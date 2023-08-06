#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
EPI MRI -processing workflows.

Originally coded by Craig Moodie. Refactored by the CRN Developers.
"""

import os
import os.path as op

from nipype.pipeline import engine as pe
from nipype.interfaces import ants
from nipype.interfaces import c3
from nipype.interfaces import io as nio
from nipype.interfaces import utility as niu
from nipype.interfaces import fsl
from nipype.interfaces import freesurfer as fs

from fmriprep.data import get_mni_template_ras
from fmriprep.interfaces import ReadSidecarJSON, DerivativesDataSink
from fmriprep.viz import stripped_brain_overlay
from fmriprep.workflows.fieldmap.se_pair_workflow import create_encoding_file
from fmriprep.workflows.sbref import _extract_wm


# pylint: disable=R0914
def epi_hmc(name='EPIHeadMotionCorrectionWorkflow', sbref_present=False, settings=None):
    """
    Performs :abbr:`HMC (head motion correction)` over the input
    :abbr:`EPI (echo-planar imaging)` image.
    """
    workflow = pe.Workflow(name=name)

    infields = ['epi', 'epi_ras', 't1_brain']
    if sbref_present:
        infields += ['sbref_brain']

    inputnode = pe.Node(niu.IdentityInterface(fields=infields),
                        name='inputnode')
    outputnode = pe.Node(niu.IdentityInterface(
        fields=['epi_brain', 'xforms', 'epi_mask', 'epi_mean']), name='outputnode')

    bet = pe.Node(fsl.BET(functional=True, frac=0.6), name='EPI_bet')

    # Head motion correction (hmc)
    hmc = pe.Node(fsl.MCFLIRT(save_mats=True), name='EPI_hmc')

    pick_1st = pe.Node(fsl.ExtractROI(t_min=0, t_size=1), name='EPIPickFirst')
    hcm2itk = pe.MapNode(c3.C3dAffineTool(fsl2ras=True, itk_transform=True),
                         iterfield=['transform_file'], name='hcm2itk')

    workflow.connect([
        (inputnode, pick_1st, [('epi_ras', 'in_file')]),
        (inputnode, bet, [('epi_ras', 'in_file')]),
        (bet, hmc, [('out_file', 'in_file')]),

        (hmc, hcm2itk, [('mat_file', 'transform_file')]),
        (pick_1st, hcm2itk, [('roi_file', 'source_file'),
                             ('roi_file', 'reference_file')]),
        (hcm2itk, outputnode, [('itk_transform', 'xforms')]),
        (hmc, outputnode, [('out_file', 'epi_brain')])
    ])

    # Calculate EPI mask on the average after HMC
    epi_mean = pe.Node(fsl.MeanImage(dimension='T'), name='EPI_hmc_mean')
    bet_hmc = pe.Node(fsl.BET(mask=True, frac=0.6), name='EPI_hmc_bet')
    workflow.connect([
        (hmc, epi_mean, [('out_file', 'in_file')]),
        (epi_mean, bet_hmc, [('out_file', 'in_file')]),
        (bet_hmc, outputnode, [('mask_file', 'epi_mask'),
                               ('out_file', 'epi_mean')])
    ])

    # If we have an SBRef, it should be the reference,
    # align to mean volume otherwise
    if sbref_present:
        workflow.connect([
            (inputnode, hmc, [('sbref_brain', 'ref_file')]),
        ])
    else:
        hmc.inputs.mean_vol = True

    # Write corrected file in the designated output dir
    ds_hmc = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='hmc'), name='DerivativesHMC')
    ds_mats = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='hmc'), name='DerivativesHMCmats')
    ds_mask = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='hmc_bmask'), name='DerivativesEPImask')

    workflow.connect([
        (inputnode, ds_hmc, [('epi', 'source_file')]),
        (inputnode, ds_mats, [('epi', 'source_file')]),
        (inputnode, ds_mask, [('epi', 'source_file')]),
        (hmc, ds_hmc, [('out_file', 'in_file')]),
        (hcm2itk, ds_mats, [('itk_transform', 'in_file')]),
        (bet_hmc, ds_mask, [('mask_file', 'in_file')]),
    ])

    return workflow

def epi_mean_t1_registration(name='EPIMeanNormalization', settings=None):
    """
    Uses FSL FLIRT with the BBR cost function to find the transform that
    maps the EPI space into the T1-space
    """
    workflow = pe.Workflow(name=name)
    inputnode = pe.Node(niu.IdentityInterface(
        fields=['epi', 'epi_mean', 't1_brain', 't1_seg']), name='inputnode'
    )
    outputnode = pe.Node(
        niu.IdentityInterface(fields=['mat_epi_to_t1']),
        name='outputnode'
    )

    # Extract wm mask from segmentation
    wm_mask = pe.Node(
        niu.Function(input_names=['in_file'], output_names=['out_file'],
        function=_extract_wm),
        name='WM_mask'
    )


    flt_bbr_init = pe.Node(fsl.FLIRT(dof=6, out_matrix_file='init.mat'),
        name='Flirt_BBR_init')
    flt_bbr = pe.Node(fsl.FLIRT(dof=6, cost_func='bbr'), name='Flirt_BBR')
    flt_bbr.inputs.schedule = settings['fsl'].get(
        'flirt_bbr', op.join(os.getenv('FSLDIR'), 'etc/flirtsch/bbr.sch'))

    # make equivalent warp fields
    invt_bbr = pe.Node(fsl.ConvertXFM(invert_xfm=True), name='Flirt_BBR_Inv')

    #  EPI to T1 transform matrix is from fsl, using c3 tools to convert to
    #  something ANTs will like.
    fsl2itk_fwd = pe.Node(c3.C3dAffineTool(fsl2ras=True, itk_transform=True),
                          name='fsl2itk_fwd')
    fsl2itk_inv = pe.Node(c3.C3dAffineTool(fsl2ras=True, itk_transform=True),
                          name='fsl2itk_inv')

    # Write EPI mean in T1w space
    ds_t1w = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='hmc_t1'), name='DerivHMC_T1w')
    # Write registrated file in the designated output dir
    ds_tfm_fwd = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='epi2t1w_affine'), name='DerivEPI_to_T1w_fwd')
    ds_tfm_inv = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='t1w2epi_affine'), name='DerivEPI_to_T1w_inv')

    workflow.connect([
        (inputnode, wm_mask, [('t1_seg', 'in_file')]),
        (inputnode, flt_bbr_init, [('t1_brain', 'reference')]),
        (inputnode, fsl2itk_fwd, [('t1_brain', 'reference_file'),
                                  ('epi_mean', 'source_file')]),
        (inputnode, fsl2itk_inv, [('epi_mean', 'reference_file'),
                                  ('t1_brain', 'source_file')]),
        (inputnode, flt_bbr_init, [('epi_mean', 'in_file')]),
        (flt_bbr_init, flt_bbr, [('out_matrix_file', 'in_matrix_file')]),
        (inputnode, flt_bbr, [('t1_brain', 'reference')]),
        (inputnode, flt_bbr, [('epi_mean', 'in_file')]),
        (wm_mask, flt_bbr, [('out_file', 'wm_seg')]),
        (flt_bbr, invt_bbr, [('out_matrix_file', 'in_file')]),
        (flt_bbr, fsl2itk_fwd, [('out_matrix_file', 'transform_file')]),
        (invt_bbr, fsl2itk_inv, [('out_file', 'transform_file')]),
        (fsl2itk_fwd, outputnode, [('itk_transform', 'mat_epi_to_t1')]),
        (fsl2itk_inv, outputnode, [('itk_transform', 'mat_t1_to_epi')]),
        (inputnode, ds_tfm_fwd, [('epi', 'source_file')]),
        (inputnode, ds_tfm_inv, [('epi', 'source_file')]),
        (inputnode, ds_t1w, [('epi', 'source_file')]),
        (fsl2itk_fwd, ds_tfm_fwd, [('itk_transform', 'in_file')]),
        (fsl2itk_inv, ds_tfm_inv, [('itk_transform', 'in_file')]),
        (flt_bbr, ds_t1w, [('out_file', 'in_file')])
    ])

    # Plots for report
    png_sbref_t1 = pe.Node(niu.Function(
        input_names=['in_file', 'overlay_file', 'out_file'],
        output_names=['out_file'],
        function=stripped_brain_overlay),
        name='PNG_sbref_t1'
    )
    png_sbref_t1.inputs.out_file = 'sbref_to_t1.png'

    # Write corrected file in the designated output dir
    ds_png = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='epi_to_t1'), name='DerivativesPNG')

    workflow.connect([
        (flt_bbr, png_sbref_t1, [('out_file', 'overlay_file')]),
        (inputnode, png_sbref_t1, [('t1_seg', 'in_file')]),
        (inputnode, ds_png, [('epi', 'source_file')]),
        (png_sbref_t1, ds_png, [('out_file', 'in_file')])
    ])

    return workflow

def epi_mni_transformation(name='EPIMNITransformation', settings=None):
    workflow = pe.Workflow(name=name)
    inputnode = pe.Node(
        niu.IdentityInterface(fields=[
            'mat_epi_to_t1',
            't1_2_mni_forward_transform',
            'epi',
            'epi_ras',
            'epi_mask',
            't1',
            'hmc_xforms'
        ]),
        name='inputnode'
    )

    def _aslist(in_value):
        if isinstance(in_value, list):
            return in_value
        return [in_value]

    pick_1st = pe.Node(fsl.ExtractROI(t_min=0, t_size=1), name='EPIPickFirst')

    gen_ref = pe.Node(niu.Function(
        input_names=['fixed_image', 'moving_image'], output_names=['out_file'],
        function=_gen_reference), name='GenNewMNIReference')
    gen_ref.inputs.fixed_image = op.join(get_mni_template_ras(),
                                         'MNI152_T1_1mm.nii.gz')

    split = pe.Node(fsl.Split(dimension='t'), name='SplitEPI')
    merge_transforms = pe.MapNode(niu.Merge(3),
                                  iterfield=['in3'], name='MergeTransforms')
    epi_to_mni_transform = pe.MapNode(
        ants.ApplyTransforms(), iterfield=['input_image', 'transforms'],
        name='EPIToMNITransform')
    epi_to_mni_transform.terminal_output = 'file'
    merge = pe.Node(fsl.Merge(dimension='t'), name='MergeEPI')

    mask_merge_tfms = pe.Node(niu.Merge(2), name='MaskMergeTfms')
    mask_mni_tfm = pe.Node(ants.ApplyTransforms(interpolation='NearestNeighbor'),
                           name='MaskToMNI')

    # Write corrected file in the designated output dir
    ds_mni = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='hmc_mni'), name='DerivativesHMCMNI')
    ds_mni_mask = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='hmc_mni_bmask'), name='DerivativesHMCMNImask')

    workflow.connect([
        (inputnode, pick_1st, [('epi_ras', 'in_file')]),
        (inputnode, ds_mni, [('epi', 'source_file')]),
        (inputnode, ds_mni_mask, [('epi', 'source_file')]),
        (pick_1st, gen_ref, [('roi_file', 'moving_image')]),
        (inputnode, merge_transforms, [('t1_2_mni_forward_transform', 'in1'),
                                       (('mat_epi_to_t1', _aslist), 'in2'),
                                       ('hmc_xforms', 'in3')]),
        (inputnode, mask_merge_tfms, [('t1_2_mni_forward_transform', 'in1'),
                                      (('mat_epi_to_t1', _aslist), 'in2')]),
        (inputnode, split, [('epi_ras', 'in_file')]),
        (split, epi_to_mni_transform, [('out_files', 'input_image')]),
        (merge_transforms, epi_to_mni_transform, [('out', 'transforms')]),
        (gen_ref, epi_to_mni_transform, [('out_file', 'reference_image')]),
        (epi_to_mni_transform, merge, [('output_image', 'in_files')]),
        (merge, ds_mni, [('merged_file', 'in_file')]),
        (mask_merge_tfms, mask_mni_tfm, [('out', 'transforms')]),
        (gen_ref, mask_mni_tfm, [('out_file', 'reference_image')]),
        (inputnode, mask_mni_tfm, [('epi_mask', 'input_image')]),
        (mask_mni_tfm, ds_mni_mask, [('output_image', 'in_file')])
    ])

    return workflow

# pylint: disable=R0914
def epi_unwarp(name='EPIUnwarpWorkflow', settings=None):
    """ A workflow to correct EPI images """
    workflow = pe.Workflow(name=name)
    inputnode = pe.Node(niu.IdentityInterface(
        fields=['epi', 'sbref_brain', 'fmap_fieldcoef', 'fmap_movpar',
                'fmap_mask', 'epi_brain']), name='inputnode')
    outputnode = pe.Node(
        niu.IdentityInterface(fields=['epi_correct', 'epi_mean']),
        name='outputnode'
    )

    # Read metadata
    meta = pe.MapNode(
        ReadSidecarJSON(fields=['TotalReadoutTime', 'PhaseEncodingDirection']),
        iterfield=['in_file'],
        name='metadata'
    )

    encfile = pe.Node(interface=niu.Function(
        input_names=['fieldmaps', 'in_dict'], output_names=['parameters_file'],
        function=create_encoding_file), name='TopUp_encfile', updatehash=True)

    fslsplit = pe.Node(fsl.Split(dimension='t'), name='EPI_split')

    # Now, we cannot use the LSR method
    unwarp_epi = pe.MapNode(fsl.ApplyTOPUP(method='jac', in_index=[1]),
                            iterfield=['in_files'], name='TopUpApply')

    # Merge back
    fslmerge = pe.Node(fsl.Merge(dimension='t'), name='EPI_corr_merge')

    # Compute mean
    epi_mean = pe.Node(fsl.MeanImage(dimension='T'), name='EPI_mean')

    workflow.connect([
        (inputnode, meta, [('epi', 'in_file')]),
        (inputnode, encfile, [('epi', 'fieldmaps')]),
        (inputnode, fslsplit, [('epi_brain', 'in_file')]),
        (meta, encfile, [('out_dict', 'in_dict')]),
        (inputnode, unwarp_epi, [('fmap_fieldcoef', 'in_topup_fieldcoef'),
                                 ('fmap_movpar', 'in_topup_movpar')]),
        (encfile, unwarp_epi, [('parameters_file', 'encoding_file')]),
        (fslsplit, unwarp_epi, [('out_files', 'in_files')]),
        (unwarp_epi, fslmerge, [('out_corrected', 'in_files')]),
        (fslmerge, epi_mean, [('merged_file', 'in_file')]),
        (fslmerge, outputnode, [('merged_file', 'epi_correct')]),
        (epi_mean, outputnode, [('out_file', 'epi_mean')])
    ])

    # Plot result
    png_epi_corr= pe.Node(niu.Function(
        input_names=['in_file', 'overlay_file', 'out_file'], output_names=['out_file'],
        function=stripped_brain_overlay), name='PNG_epi_corr')
    png_epi_corr.inputs.out_file = 'corrected_EPI.png'

    ds_png = pe.Node(
        DerivativesDataSink(base_directory=settings['output_dir'],
            suffix='sdc'), name='DerivativesPNG')

    workflow.connect([
        (epi_mean, png_epi_corr, [('out_file', 'overlay_file')]),
        (inputnode, png_epi_corr, [('fmap_mask', 'in_file')]),
        (inputnode, ds_png, [('epi', 'source_file')]),
        (png_epi_corr, ds_png, [('out_file', 'in_file')])
    ])

    return workflow


def _gen_reference(fixed_image, moving_image, out_file=None):
    import os.path as op
    import numpy as np
    import nibabel as nb
    from nibabel.affines import apply_affine

    if out_file is None:
        fname, ext = op.splitext(op.basename(fixed_image))
        if ext == '.gz':
            fname, ext2 = op.splitext(fname)
            ext = ext2 + ext
        out_file = op.abspath('%s_wm%s' % (fname, ext))

    imref = nb.load(fixed_image)
    immov = nb.load(moving_image)

    orig = apply_affine(imref.affine, [-0.5] * 3)
    end = apply_affine(imref.affine, [s - 0.5 for s in imref.get_data().shape[:3]])

    mov_spacing = immov.get_header().get_zooms()[:3]
    new_sizes = np.ceil((end-orig)/mov_spacing)

    new_affine = immov.affine
    ref_center = apply_affine(imref.affine, (0.5 * (np.array(imref.get_data().shape[:3]))))

    new_center = new_affine[:3, :3].dot(new_sizes)
    new_affine[:3, 3] = -0.5 * new_center + ref_center

    new_ref_im = nb.Nifti1Image(np.zeros(tuple(new_sizes.astype(int))),
                                new_affine, immov.get_header())
    new_ref_im.to_filename(out_file)

    return out_file
