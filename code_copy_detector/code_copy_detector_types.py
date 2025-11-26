import tokenize
from dataclasses import dataclass
from typing import Dict, List, Tuple

# Type alias for a token list (List of TokenInfo objects)
TokenList = List[tokenize.TokenInfo]

# Type alias for an n-gram (Tuple of n TokenInfo objects)
NGram = Tuple[tokenize.TokenInfo, ...]

@dataclass
class NGramData:
    file: str
    ngram: List[NGram]

# Type alias for the token type tuple (keys in the dictionary)
TokenTypeTuple = Tuple[int, ...]

# Type alias for the final n-gram dictionary
NGramDict = Dict[TokenTypeTuple, List[NGramData]]