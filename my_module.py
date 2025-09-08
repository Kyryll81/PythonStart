from collections import defaultdict, Counter


def find_first_unique_char(text: str) -> str | None:
    if not isinstance(text, str):
        raise TypeError()
    
    cache_text: defaultdict = defaultdict(dict)
    
    if text in cache_text.keys():
        return cache_text[text]
    
    for key, value in Counter(text).items():
        if value == 1:
            cache_text[text] = key
            return cache_text[text]
    
    cache_text[text] = None
    return cache_text[text]        
