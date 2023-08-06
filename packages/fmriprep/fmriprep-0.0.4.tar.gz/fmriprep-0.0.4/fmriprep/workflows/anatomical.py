#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Anatomical Reference -processing workflows.

Originally coded by Craig Moodie. Refactored by the CRN Developers.

"""
import os
import os.path as op
import pkg_resources as pkgr

from nipype.interfaces import ants
from nipype.interfaces import fsl
from nipype.interfaces import freesurfer as fs
from nipype.interfaces import io as nio
from nipype.interfaces import utility as niu
from nipype.pipeline import engine as pe

from niworkflows.anat.skullstrip import afni_wf as skullstrip_wf
from niworkflows.common import reorient as mri_reorient_wf

from fmriprep.data import get_ants_oasis_template_ras, get_mni_template_ras
from fmriprep.viz import stripped_brain_overlay, anatomical_overlay


#  pylint: disable=R0914
def t1w_preprocessing(name='t1w_preprocessing', settings=None):
    """T1w images preprocessing pipeline"""

    if settings is None:
        raise RuntimeError('Workflow settings are missing')

    workflow = pe.Workflow(name=name)

    inputnode = pe.Node(niu.IdentityInterface(fields=['t1']), name='inputnode')
    outputnode = pe.Node(niu.IdentityInterface(
        fields=['t1_seg', 'bias_corrected_t1', 't1_brain', 't1_2_mni',
                't1_2_mni_forward_transform', 't1_2_mni_reverse_transform',
                't1_segmentation']), name='outputnode')

    # 1. Reorient T1
    arw = pe.Node(fs.MRIConvert(out_type='niigz', out_orientation='RAS'), name='Reorient')

    # 2. T1 Bias Field Correction
    inu_n4 = pe.Node(ants.N4BiasFieldCorrection(dimension=3), name='Bias_Field_Correction')

    # 3. Skull-stripping
    asw = skullstrip_wf()
    if settings.get('skull_strip_ants', False):
        asw = skullstrip_ants(settings=settings)

    # 4. Segmentation
    t1_seg = pe.Node(fsl.FAST(no_bias=True), name='T1_Segmentation')

    # 5. T1w to MNI registration
    t1_2_mni = pe.Node(ants.Registration(), name='T1_2_MNI_Registration')
    t1_2_mni.inputs.collapse_output_transforms = False
    t1_2_mni.inputs.write_composite_transform = False
    t1_2_mni.inputs.output_transform_prefix = 'T1_to_MNI_'
    t1_2_mni.inputs.output_warped_image = 't1_to_mni.nii.gz'
    t1_2_mni.inputs.num_threads = 4
    t1_2_mni.inputs.fixed_image = op.join(get_mni_template_ras(), 'MNI152_T1_1mm.nii.gz')
    t1_2_mni.inputs.fixed_image_mask = op.join(
        get_mni_template_ras(), 'MNI152_T1_1mm_brain_mask.nii.gz')

    # Hack to avoid re-running ANTs all the times
    grabber_interface = nio.JSONFileGrabber()
    setattr(grabber_interface, '_always_run', False)
    t1_2_mni_params = pe.Node(grabber_interface, name='t1_2_mni_params')
    t1_2_mni_params.inputs.in_file = (
        pkgr.resource_filename('fmriprep', 'data/{}.json'.format(
            settings.get('ants_t1-mni_settings', 't1-mni_registration2')))
    )

    workflow.connect([
        (inputnode, arw, [('t1', 'in_file')]),
        (arw, inu_n4, [('out_file', 'input_image')]),
        (inu_n4, asw, [('output_image', 'inputnode.in_file')]),
        (asw, t1_seg, [('outputnode.out_file', 'in_files')]),
        (inu_n4, t1_2_mni, [('output_image', 'moving_image')]),
        (asw, t1_2_mni, [('outputnode.out_mask', 'moving_image_mask')]),
        (t1_seg, outputnode, [('tissue_class_map', 't1_seg')]),
        (inu_n4, outputnode, [('output_image', 'bias_corrected_t1')]),
        (t1_seg, outputnode, [('tissue_class_map', 't1_segmentation')]),
        (t1_2_mni, outputnode, [
            ('warped_image', 't1_2_mni'),
            ('forward_transforms', 't1_2_mni_forward_transform'),
            ('reverse_transforms', 't1_2_mni_reverse_transform')
        ]),
        (asw, outputnode, [
            ('outputnode.out_file', 't1_brain')]),
    ])

    # Connect reporting nodes
    t1_stripped_overlay = pe.Node(niu.Function(
        input_names=['in_file', 'overlay_file', 'out_file'], output_names=['out_file'],
        function=stripped_brain_overlay), name='PNG_T1_SkullStrip')
    t1_stripped_overlay.inputs.out_file = 't1_stripped_overlay.png'

    # The T1-to-MNI will be plotted using the segmentation. That's why we transform it first
    seg_2_mni = pe.Node(ants.ApplyTransforms(
        dimension=3, default_value=0, interpolation='NearestNeighbor'), name='T1_2_MNI_warp')
    seg_2_mni.inputs.reference_image = op.join(get_mni_template_ras(), 'MNI152_T1_1mm.nii.gz')

    t1_2_mni_overlay = pe.Node(niu.Function(
        input_names=['in_file', 'overlay_file', 'out_file'], output_names=['out_file'],
        function=stripped_brain_overlay), name='PNG_T1_to_MNI')
    t1_2_mni_overlay.inputs.out_file = 't1_to_mni_overlay.png'
    t1_2_mni_overlay.inputs.overlay_file = op.join(get_mni_template_ras(), 'MNI152_T1_1mm.nii.gz')

    datasink = pe.Node(
        interface=nio.DataSink(
            base_directory=op.join(settings['output_dir'], 'images')),
        name='datasink',
        parameterization=False
    )

    workflow.connect([
        (inu_n4, t1_stripped_overlay, [('output_image', 'overlay_file')]),
        (asw, t1_stripped_overlay, [('outputnode.out_mask', 'in_file')]),
        (t1_stripped_overlay, datasink, [('out_file', '@t1_stripped_overlay')]),
        (t1_seg, seg_2_mni, [('tissue_class_map', 'input_image')]),
        (t1_2_mni, seg_2_mni, [('forward_transforms', 'transforms'),
                               ('forward_invert_flags', 'invert_transform_flags')]),
        (seg_2_mni, t1_2_mni_overlay, [('output_image', 'in_file')]),
        (t1_2_mni_overlay, datasink, [('out_file', '@t1_2_mni_overlay')]),
    ])

    # ANTs inputs connected here for clarity
    workflow.connect([
        (t1_2_mni_params, t1_2_mni, [
            ('metric', 'metric'),
            ('metric_weight', 'metric_weight'),
            ('dimension', 'dimension'),
            ('write_composite_transform', 'write_composite_transform'),
            ('radius_or_number_of_bins', 'radius_or_number_of_bins'),
            ('shrink_factors', 'shrink_factors'),
            ('smoothing_sigmas', 'smoothing_sigmas'),
            ('sigma_units', 'sigma_units'),
            ('output_transform_prefix', 'output_transform_prefix'),
            ('transforms', 'transforms'),
            ('transform_parameters', 'transform_parameters'),
            ('initial_moving_transform_com', 'initial_moving_transform_com'),
            ('number_of_iterations', 'number_of_iterations'),
            ('convergence_threshold', 'convergence_threshold'),
            ('convergence_window_size', 'convergence_window_size'),
            ('sampling_strategy', 'sampling_strategy'),
            ('sampling_percentage', 'sampling_percentage'),
            ('output_warped_image', 'output_warped_image'),
            ('use_histogram_matching', 'use_histogram_matching'),
            ('use_estimate_learning_rate_once',
             'use_estimate_learning_rate_once'),
            ('collapse_output_transforms', 'collapse_output_transforms'),
            ('winsorize_lower_quantile', 'winsorize_lower_quantile'),
            ('winsorize_upper_quantile', 'winsorize_upper_quantile'),
        ])
    ])

    return workflow


def skullstrip_ants(name='ANTsBrainExtraction', settings=None):
    if settings is None:
        settings = {'debug': False}

    workflow = pe.Workflow(name=name)

    inputnode = pe.Node(niu.IdentityInterface(fields=['in_file']), name='inputnode')
    outputnode = pe.Node(niu.IdentityInterface(
        fields=['out_file', 'out_mask']), name='outputnode')


    t1_skull_strip = pe.Node(ants.segmentation.BrainExtraction(
        dimension=3, use_floatingpoint_precision=1,
        debug=settings['debug']), name='Ants_T1_Brain_Extraction')
    t1_skull_strip.inputs.brain_template = op.join(get_ants_oasis_template_ras(),
                                                   'T_template0.nii.gz')
    t1_skull_strip.inputs.brain_probability_mask = op.join(
        get_ants_oasis_template_ras(),
        'T_template0_BrainCerebellumProbabilityMask.nii.gz'
    )
    t1_skull_strip.inputs.extraction_registration_mask = op.join(
        get_ants_oasis_template_ras(),
        'T_template0_BrainCerebellumRegistrationMask.nii.gz'
    )

    workflow.connect([
        (inputnode, t1_skull_strip, [('in_file', 'anatomical_image')]),
        (t1_skull_strip, outputnode, [('BrainExtractionMask', 'out_mask'),
                                      ('BrainExtractionBrain', 'out_file')])
    ])

    return workflow
