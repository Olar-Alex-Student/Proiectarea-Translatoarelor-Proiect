import re

def extract_with_regex(pattern, text):
    return re.findall(pattern, text)
