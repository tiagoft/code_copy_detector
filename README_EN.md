# Code Copy Detector

A detector for copied code

If you are going to *develop* from this repository, go to the [development guide](README_DEV.md).

## Installing Code Copy Detector:

Remember to follow these instructions from within your preferred virtual environment:

    conda create -n code_copy_detector python=3.11
    conda activate code_copy_detector

The first way is to clone the repository and do a local installation:

    git clone https://github.com/tiagoft/code_copy_detector.git
    cd code_copy_detector
    pip install .

The second way is to install directly:

    pip install git+https://github.com/tiagoft/code_copy_detector.git

To uninstall, use:

    pip uninstall code_copy_detector

## Usage

To find all implemented commands, run:

    code_copy_detector-cli --help
