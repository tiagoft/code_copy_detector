"""
Detect code copies in source code files
"""

from rich.console import Console
import typer

import code_copy_detector as ccd
import os
from itertools import combinations

app = typer.Typer(no_args_is_help=True)
console = Console()

@app.command('info')
def print_info(custom_message : str = ""):
    """
    Print information about the module
    """
    console.print("Hello! I am Code Copy Detector")
    console.print(f"Author: { ccd.__author__}")
    console.print(f"Version: { ccd.__version__}")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")

@app.command('compare') # Defines a default action
def compare_files(fname1: str, fname2: str, ngram_length: int = 20):
    """
    Compares two source codes and searches for similarities
    """
    tokenlist = ccd.get_token_list(fname1)
    ngrams = ccd.get_token_ngrams(tokenlist, ngram_length)
    ngram_dict = ccd.make_ngram_dictionary(ngrams, fname1)
    tokenlist2 = ccd.get_token_list(fname2)
    ngrams2 = ccd.get_token_ngrams(tokenlist2, ngram_length)
    ngram_dict2 = ccd.make_ngram_dictionary(ngrams2, fname2)
    _, n_copies, len_dict_1, len_dict_2 = ccd.compare_ngram_dictionaries(
        ngram_dict, ngram_dict2)
    console.print(f"Found {n_copies} copies of code")
    console.print(f"This corresponds to {n_copies/len_dict_1:.2%} of the first file ({fname1})")
    console.print(f"This corresponds to {n_copies/len_dict_2:.2%} of the first file ({fname2})")

@app.command('comparedir')
def compare_directory(directory : str, ngram_length: int = 20, threshold: float = 0.6, output_dot: bool = False):
    """
    Compares all pairs of files in a directory
    """
    # Get all .py and .ipynb files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]


    output_dict = {}
    # Compare all pairs of files
    for fname1, fname2 in combinations(files, 2):
        try:
            tokenlist = ccd.get_token_list(fname1)
        except IndentationError:
            console.print(f"Could not read {fname1}")
            continue
        ngrams = ccd.get_token_ngrams(tokenlist, ngram_length)
        ngram_dict = ccd.make_ngram_dictionary(ngrams, fname1)
        try:
            tokenlist2 = ccd.get_token_list(fname2)
        except IndentationError:
            console.print(f"Could not read {fname2}")
            continue
        ngrams2 = ccd.get_token_ngrams(tokenlist2, ngram_length)
        ngram_dict2 = ccd.make_ngram_dictionary(ngrams2, fname2)
        _, n_copies, len_dict_1, len_dict_2 = ccd.compare_ngram_dictionaries(
            ngram_dict, ngram_dict2)
        if n_copies/len_dict_1 > threshold or n_copies/len_dict_2 > threshold:
            output_dict[(fname1, fname2)] = (n_copies, len_dict_1, len_dict_2)

    if output_dot:
        str_out = ccd.results_to_dot(output_dict)
        console.print(str_out)
    else:
        for results in output_dict:
            console.print(f"Found {output_dict[results][0]} copies between {results[0]} and {results[1]}")
            console.print(f"This corresponds to {output_dict[results][0]/output_dict[results][1]:.2%} of the first file ({results[0]})")
            console.print(f"This corresponds to {output_dict[results][0]/output_dict[results][2]:.2%} of the second file ({results[1]})")


@app.command('jupyter_to_py')
def convert_jupyter_to_py(directory: str, recurse_and_rename : bool = False):
    """
    Converts all Jupyter notebooks in directory to Python files
    """
    current_working_directory = os.getcwd()
    if recurse_and_rename:
        files = []
        
        print(current_working_directory)

        for root, _, filenames in os.walk(current_working_directory):
            for filename in filenames:
                if filename.endswith('.ipynb'):
                    files.append(os.path.join(root, filename))
    else:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.ipynb')]
    

    for fname in files:
        console.print(f'Converting {fname} to Python')
        ccd.jupyter_to_py(fname, fname.replace(current_working_directory, '').replace('.ipynb', '.py').replace('/', '_').lstrip('_'))

if __name__ == "__main__":
    app()
