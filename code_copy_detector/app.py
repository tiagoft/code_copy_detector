import code_copy_detector as ccd
from typing import Optional, List, Tuple, Dict
import os
from itertools import combinations
from code_copy_detector.code_copy_detector_types import TokenList, NGramDict

class CodeCopyDetectorApp:
    @staticmethod
    def get_token_list_for_file(fname: str) -> Optional[TokenList]:
        try:
            tokenlist = ccd.get_token_list(fname)
            return tokenlist
        except IndentationError:
            return None
        
    @staticmethod
    def make_ngram_dictionary_of_file(
        fname: str, 
        ngram_length: int = 20, 
        stop_ngrams: Optional[dict] = None
    ) -> Optional[NGramDict]:
        tokenlist = CodeCopyDetectorApp.get_token_list_for_file(fname)
        if not tokenlist:
            return None
        ngrams = ccd.get_token_ngrams(tokenlist, ngram_length)
        return ccd.make_ngram_dictionary(ngrams, fname, stop_ngrams=stop_ngrams)
    
    @staticmethod
    def compare_files(
        fname1: str, 
        fname2: str, 
        ngram_length: int = 20, 
        base_file: Optional[str] = None
    ) -> Tuple[int, int, int]:
        stopngram_dict = None
        if base_file:
            stopngram_dict = CodeCopyDetectorApp.make_ngram_dictionary_of_file(base_file)

        ngram_dict1 = CodeCopyDetectorApp.make_ngram_dictionary_of_file(fname1, ngram_length, stopngram_dict)
        ngram_dict2 = CodeCopyDetectorApp.make_ngram_dictionary_of_file(fname2, ngram_length, stopngram_dict)

        if not ngram_dict1 or not ngram_dict2:
            return 0, None, None

        _, n_copies, len_dict_1, len_dict_2 = ccd.compare_ngram_dictionaries(
            ngram_dict1, ngram_dict2)
        
        return n_copies, len_dict_1, len_dict_2
    
    @staticmethod
    def compare_directory(
        directory: str,
        ngram_length: int = 20,
        threshold: float = 0.6,
        base_file: Optional[str] = None,
    ) -> Tuple[Dict[Tuple[str, str], Tuple[int, int, int]], set]:
        stopngram_dict = None
        if base_file:
            stopngram_dict = CodeCopyDetectorApp.make_ngram_dictionary_of_file(base_file)

        # Get all .py and .ipynb files in the directory
        files = [
            os.path.join(directory, f) for f in os.listdir(directory)
            if f.endswith('.py')
        ]

        output_dict = {}
        failed_files = []
        # Compare all pairs of files
        for fname1, fname2 in combinations(files, 2):
            
            ngram_dict1 = CodeCopyDetectorApp.make_ngram_dictionary_of_file(fname1, ngram_length, stopngram_dict)
            if not ngram_dict1:
                failed_files.append(fname1)
                continue

            ngram_dict2 = CodeCopyDetectorApp.make_ngram_dictionary_of_file(fname2, ngram_length, stopngram_dict)
            if not ngram_dict2:
                failed_files.append(fname2)
                continue


            _, n_copies, len_dict_1, len_dict_2 = ccd.compare_ngram_dictionaries(
                ngram_dict1, ngram_dict2)
            
            if n_copies / len_dict_1 > threshold or n_copies / len_dict_2 > threshold:
                output_dict[(fname1, fname2)] = (n_copies, len_dict_1, len_dict_2)

        return output_dict, set(failed_files)
        
    @staticmethod
    def find_all_jupyter_notebooks(directory: str, recurse_and_rename: bool = False) -> List[str]:
        current_working_directory = os.getcwd()
        if recurse_and_rename:
            files = []

            print(current_working_directory)

            for root, _, filenames in os.walk(current_working_directory):
                for filename in filenames:
                    if filename.endswith('.ipynb'):
                        files.append(os.path.join(root, filename))
        else:
            files = [
                os.path.join(directory, f) for f in os.listdir(directory)
                if f.endswith('.ipynb')
            ]

        return files
    
    @staticmethod
    def jupyter_to_py(fname: str) -> None:
        current_working_directory = os.getcwd()
        ccd.jupyter_to_py(
            fname,
            fname.replace(current_working_directory,
                          '').replace('.ipynb',
                                      '.py').replace('/', '_').lstrip('_'))