# Developer Guide

## Setting Up Your Development Environment

Run these instructions immediately after creating your project with cookiecutter.

1. Navigate to the directory you created:

        cd code_copy_detector

2. Create and activate a virtual environment for your development:

        conda create -n code_copy_detector python=3.11
        conda activate code_copy_detector

3. **Install `uv` and the `gh` application (optional)**

   Install the `uv` package manager and the `gh` application (GitHub CLI):

        conda install uv gh --channel conda-forge
        gh auth login

4. **Install your module in editable mode with `uv`:**

   `uv` is used here to install the package in editable mode (`-e .`):

        uv pip install -e .

5. Verify that the command-line tool is functional:

        code_copy_detector-cli --help

## Syncing with GitHub

### Using the `gh` application

In the root folder of your newly created project:

    git init
    git add *
    git commit -m "Initial commit"
    gh repo create code_copy_detector --public --push --source .

### Without the `gh` application

1. In your browser, go to [GitHub](https://www.github.com) and log in.
1. Create a new repository (empty, no initial README, no gitignore, etc.) named **code_copy_detector** (remember to respect case sensitivity, etc.).
1. Execute the commands below in the root folder of your newly created project:

        git init
        git add *
        git commit -m "Initial commit"
        git remote add origin https://github.com/<YOUR-GITHUB-USERNAME>/code_copy_detector.git
        git push --set-upstream origin main