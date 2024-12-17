import re

def extract_with_regex(pattern, text):
    """Extrage toate potrivirile pentru un regex dintr-un text."""
    return re.findall(pattern, text)
