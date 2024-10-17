import code_copy_detector as ccd
import os
from pathlib import Path
from rich.console import Console
import typer

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
def run(fname1: str, fname2: str, ngram_length: int = 20):
    """
    Compares two source codes and searches for similarities
    """
    tokenlist = ccd.get_token_list(fname1)
    ngrams = ccd.get_token_ngrams(tokenlist, ngram_length)
    ngram_dict = ccd.make_ngram_dictionary(ngrams, fname1)
    tokenlist2 = ccd.get_token_list(fname2)
    ngrams2 = ccd.get_token_ngrams(tokenlist2, ngram_length)
    ngram_dict2 = ccd.make_ngram_dictionary(ngrams2, fname2)
    shared_ngrams, n_copies, len_dict_1, len_dict_2 = ccd.compare_ngram_dictionaries(
        ngram_dict, ngram_dict2)
    console.print(f"Found {n_copies} copies of code")
    console.print(f"This corresponds to {n_copies/len_dict_1:.2%} of the first file ({fname1})")
    console.print(f"This corresponds to {n_copies/len_dict_2:.2%} of the first file ({fname2})")

if __name__ == "__main__":
    app()
