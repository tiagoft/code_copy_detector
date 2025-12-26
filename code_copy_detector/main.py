"""
Detect code copies in source code files
"""

import os
from typing import Optional

import typer
from rich.console import Console

import code_copy_detector as ccd
from code_copy_detector.app import CodeCopyDetectorApp


app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command('info')
def print_info(custom_message: str = "") -> None:
    """
    Print information about the module
    """
    console.print("Hello! I am Code Copy Detector")
    console.print(f"Author: { ccd.__author__}")
    console.print(f"Version: { ccd.__version__}")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")


@app.command('compare')  # Defines a default action
def compare_files(
    fname1: str,
    fname2: str,
    ngram_length: int = 20,
    base_file: Optional[str] = None
) -> None:
    """
    Compares two source codes and searches for similarities
    """
    n_copies, len_dict_1, len_dict_2 = CodeCopyDetectorApp.compare_files(fname1, fname2, ngram_length, base_file)

    if not len_dict_1 or not len_dict_2:
        console.print("Could not compare files")
        if not len_dict_1:
            console.print(f"Could not read {fname1}")
        if not len_dict_2:
            console.print(f"Could not read {fname2}")
        return

    console.print(f"Found {n_copies} copies of code")
    console.print(
        f"This corresponds to {n_copies/len_dict_1:.2%} of the first file ({fname1})"
    )
    console.print(
        f"This corresponds to {n_copies/len_dict_2:.2%} of the first file ({fname2})"
    )


@app.command('comparedir')
def compare_directory(
    directory: str,
    ngram_length: int = 20,
    threshold: float = 0.6,
    output_dot: bool = False,
    base_file: Optional[str] = None
) -> None:
    """
    Compares all pairs of files in a directory
    """

    output_dict, failed_files = CodeCopyDetectorApp.compare_directory(directory, ngram_length, threshold, base_file)

    for failed_file in failed_files:
        console.print(f"Could not read {failed_file}")

    if output_dot:
        str_out = ccd.results_to_dot(output_dict)
        console.print(str_out)
    else:
        for results in output_dict:
            console.print(f"Comparing {results[0]} with {output_dict[results][0]} ngrams and {results[1]} with {output_dict[results][1]} ngrams")
            console.print(
                f"Found {output_dict[results][0]} copies between {results[0]} and {results[1]}"
            )
            console.print(
                f"This corresponds to {output_dict[results][0]/output_dict[results][1]:.2%} of the first file ({results[0]})"
            )
            console.print(
                f"This corresponds to {output_dict[results][0]/output_dict[results][2]:.2%} of the second file ({results[1]})"
            )


@app.command('jupyter_to_py')
def convert_jupyter_to_py(directory: str, recurse_and_rename: bool = False) -> None: 
    """
    Converts all Jupyter notebooks in directory to Python files
    """
    files = CodeCopyDetectorApp.find_all_jupyter_notebooks(directory, recurse_and_rename)

    for fname in files:
        console.print(f'Converting {fname} to Python')
        CodeCopyDetectorApp.jupyter_to_py(fname)

if __name__ == "__main__":
    app()
