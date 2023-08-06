from future.utils import raise_from

from nipype.pipeline import Workflow

from fmriprep.workflows.fieldmap.fieldmap_to_phasediff import fieldmap_to_phasediff
from fmriprep.workflows.fieldmap.se_pair_workflow import se_pair_workflow
from fmriprep.workflows.fieldmap.phase_diff_and_magnitudes import phase_diff_and_magnitudes
from fmriprep.workflows.fieldmap.helper import (is_fmap_type)

def fieldmap_decider(subject_data, settings):
    ''' Initialize FieldmapDecider to automatically find a
    Fieldmap preprocessing workflow '''

    # POSSIBLE FILES ACCORDING TO BIDS 1.0.0
    # 8.9.1 one phase diff image, at least one magnitude image
    # 8.9.2 two phase images, two magnitude images
    # 8.9.3 fieldmap image (and one magnitude image)
    # 8.9.4 multiple phase encoded directions (topup)

    # inputs = { 'fieldmaps': None }
    # outputs = { 'fieldmaps': None,
    #             'outputnode.mag_brain': None,
    #             'outputnode.fmap_mask': None,
    #             'outputnode.fmap_fieldcoef': None,
    #             'outputnode.fmap_movpar': None}

    try:
        subject_data['fieldmaps'][0]
    except IndexError as e:
        raise_from(NotImplementedError("No fieldmap data found"), e)

    for filename in subject_data['fieldmaps']:
        if is_fmap_type('phasediff', filename): # 8.9.1
            return phase_diff_and_magnitudes()
        elif is_fmap_type('phase', filename): # 8.9.2
            raise NotImplementedError("No workflow for phase fieldmap data")
        elif is_fmap_type('fieldmap', filename): # 8.9.3
            return fieldmap_to_phasediff(settings=settings)
        elif is_fmap_type('topup', filename): # 8.0.4
            return se_pair_workflow(settings=settings)

    raise IOError("Unrecognized fieldmap structure")
