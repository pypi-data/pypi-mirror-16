#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
This pipeline is developed by the Poldrack lab at Stanford University
(https://poldracklab.stanford.edu/) for use at
the Center for Reproducible Neuroscience (http://reproducibility.stanford.edu/),
as well as for open-source software distribution.
"""

__version__ = '0.1.1'


__author__ = 'The CRN developers'
__copyright__ = 'Copyright 2016, Center for Reproducible Neuroscience, Stanford University'
__credits__ = ['Craig Moodie', 'Ross Blair', 'Oscar Esteban', 'Chris F. Gorgolewski',
               'Russell A. Poldrack']
__license__ = '3-clause BSD'
__maintainer__ = 'Ross Blair'
__email__ = 'crn.poldracklab@gmail.com'
__status__ = 'Prototype'
__url__ = 'https://github.com/poldracklab/preprocessing-workflow'
__packagename__ = 'fmriprep'

__description__ = """Fmriprep is a functional magnetic resonance image pre-processing pipeline that
is designed to provide an easily accessible, state-of-the-art interface that is robust to differences
in scan acquisition protocols and that requires minimal user input, while providing easily interpretable
and comprehensive error and output reporting."""
__longdesc__ = """
This package is a functional magnetic resonance image preprocessing pipeline that is designed to
provide an easily accessible, state-of-the-art interface that is robust to differences in scan
acquisition protocols and that requires minimal user input, while providing easily interpretable
and comprehensive error and output reporting. This open-source neuroimaging data processing tool
is being developed as a part of the MRI image analysis and reproducibility platform offered by the
CRN. This pipeline is heavily influenced by the `Human Connectome Project analysis pipelines
<https://github.com/Washington-University/Pipelines>`_ and, as such, the backbone of this pipeline
is a python reimplementation of the HCP `GenericfMRIVolumeProcessingPipeline.sh` script. However, a
major difference is that this pipeline is executed using a `nipype workflow framework
<http://nipype.readthedocs.io/en/latest/>`_. This allows for each call to a software module or binary
to be controlled within the workflows, which removes the need for manual curation at every stage, while
still providing all the output and error information that would be necessary for debugging and interpretation
purposes. The fmriprep pipeline primarily utilizes FSL tools, but also utilizes ANTs tools at several stages
such as skull stripping and template registration. This pipeline was designed to provide the best software
implementation for each state of preprocessing, and will be updated as newer and better neuroimaging software
become available.
"""
