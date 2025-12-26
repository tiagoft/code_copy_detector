import tokenize
from typing import Dict, List, Optional, Set, Tuple
from code_copy_detector.code_copy_detector_types import NGram, NGramData, TokenList, TokenTypeTuple, NGramDict


def get_token_list(fname: str, remove_imports: bool = True, remove_comments: bool = True) -> TokenList:
    with tokenize.open(fname) as f:
        tokens = tokenize.generate_tokens(f.readline)
        tokenlist = [token for token in tokens]
        tokenlist = [token for token in tokenlist if token.type != tokenize.NL]
        tokenlist = [token for token in tokenlist if token.type != tokenize.NEWLINE]
    if remove_imports:
        tokenlist = [token for token in tokenlist if not token.line.startswith('import')]
        tokenlist = [token for token in tokenlist if not token.line.startswith('from')]
    if remove_comments:
        tokenlist = [token for token in tokenlist if token.type != tokenize.COMMENT]
    return tokenlist

def get_token_ngrams(tokenlist: TokenList, n: int) -> List[NGram]:
    ngrams = []
    for i in range(len(tokenlist) - n + 1):
        ngram = tuple(tokenlist[i:i + n])
        ngrams.append(ngram)
    return ngrams

def get_all_token_ngrams(tokenlist: TokenList, min_n: int, max_n: int) -> List[List[NGram]]:
    all_ngrams = []
    for n in range(min_n, max_n+1):
        ngrams = get_token_ngrams(tokenlist, n)
        all_ngrams.append(ngrams)
    return all_ngrams

def make_ngram_dictionary(ngrams: List[NGram], filename: str, stop_ngrams: Optional[Set[TokenTypeTuple]] = None) -> NGramDict:
    if stop_ngrams is None:
        stop_ngrams = set()
    ngram_dict = {}
    for ngram in ngrams:
        tokentypes = tuple( [token.type for token in ngram] )
        data = NGramData(file=filename, ngram=ngrams)
        if tokentypes in stop_ngrams:
            continue
        if ngram in ngram_dict:
            ngram_dict[tokentypes].append(data)
        else:
            ngram_dict[tokentypes] = [data]
    return ngram_dict

def compare_ngram_dictionaries(dict1: NGramDict, dict2: NGramDict) -> Tuple[Dict[TokenTypeTuple, Tuple[List[NGramData], List[NGramData]]], int, int, int]:
    shared_ngrams = {}
    for ngram in dict1:
        if ngram in dict2:
            shared_ngrams[ngram] = (dict1[ngram], dict2[ngram])
    return shared_ngrams, len(shared_ngrams), len(dict1), len(dict2)