import tokenize
from dataclasses import dataclass

def get_token_list(fname, remove_imports = True, remove_comments = True):
    with tokenize.open(fname) as f:
        tokens = tokenize.generate_tokens(f.readline)
        tokenlist = [token for token in tokens if token.type != tokenize.NL]
    if remove_imports:
        tokenlist = [token for token in tokenlist if not token.line.startswith('import')]
        tokenlist = [token for token in tokenlist if not token.line.startswith('from')]
    if remove_comments:
        tokenlist = [token for token in tokenlist if token.type != tokenize.COMMENT]
    return tokenlist

def get_token_ngrams(tokenlist, n):
    ngrams = []
    for i in range(len(tokenlist) - n + 1):
        ngram = tuple(tokenlist[i:i + n])
        ngrams.append(ngram)
    return ngrams

def get_all_token_ngrams(tokenlist, min_n, max_n):
    all_ngrams = []
    for n in range(min_n, max_n+1):
        ngrams = get_token_ngrams(tokenlist, n)
        all_ngrams.append(ngrams)
    return all_ngrams



@dataclass
class NGramData:
    file: str
    ngram: list

def make_ngram_dictionary(ngrams, filename):
    ngram_dict = {}
    for ngram in ngrams:
        tokentypes = tuple( [token.type for token in ngram] )
        data = NGramData(file=filename, ngram=ngrams)
        if ngram in ngram_dict:
            ngram_dict[tokentypes].append(data)
        else:
            ngram_dict[tokentypes] = [data]
    return ngram_dict

def compare_ngram_dictionaries(dict1, dict2):
    shared_ngrams = {}
    for ngram in dict1:
        if ngram in dict2:
            shared_ngrams[ngram] = (dict1[ngram], dict2[ngram])
    return shared_ngrams, len(shared_ngrams), len(dict1), len(dict2)