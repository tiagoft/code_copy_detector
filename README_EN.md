# Code Copy Detector

A detector for copied code.

If you are going to **develop** from this repository, go to the [development guide](README_DEV_EN.md).

---

## Installing Code Copy Detector:

Remember to follow these instructions from within your preferred virtual environment. We recommend using **`uv`** for environment and package management.

### Environment Setup:

Please, prefer python 3.13 for development and installation.

* **Linux/macOS:**
    ```bash
    uv venv <YOUR-VENV-NAME> --python 3.13
    source <YOUR-VENV-NAME>/bin/activate
    ```
* **Windows (Command Prompt):**
    ```bash
    uv venv <YOUR-VENV-NAME> --python 3.13
    <YOUR-VENV-NAME>\Scripts\activate
    ```
> **Note:** Replace `<YOUR-VENV-NAME>` with your desired name (e.g., `ccd-venv`).

### Installation

The first way is to clone the repository and do a local installation:

    git clone https://github.com/tiagoft/code_copy_detector.git
    cd code_copy_detector
    uv pip install .

The second way is to install directly:

    uv pip install git+https://github.com/tiagoft/code_copy_detector.git

To uninstall, use:

    uv pip uninstall code_copy_detector

## Usage

### Compare Two Source Files

    code_copy_detector-cli compare code1.py code2.py

### Compare Code in a Directory

    code_copy_detector-cli comparedir path/to/directory --threshold=0.8 --ngram-length=10

* Adjust the `threshold` to avoid too many unnecessary lines on the screen.
* Adjust the `ngram-length` to set the window size (between 10 and 20 seem to be reasonable values).

### Generate a Graph Showing Code Similarity

This functionality helps visualize code-sharing communities:

    code_copy_detector-cli comparedir path/to/directory --threshold=0.8 --ngram-length=10 --output-dot > output.dot
    dot -Tpdf input.dot -o output.pdf

### To Find All Implemented Commands, Run:

    code_copy_detector-cli --help