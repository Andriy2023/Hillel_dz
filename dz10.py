"""Searching the small letters with three capital english letters."""

import re


def find_letters_with_conditions(filename):
    """
    Тhe function opens a text file.

    Read and search the necessary letters
    according to the pattern.
    """
    with open(filename, 'r') as f:
        text = f.read()
    pattern = r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])'
    result_find = re.findall(pattern, text)
    return result_find


filename = 'input_10.txt'
result_find = find_letters_with_conditions(filename)
output = 'Result: \"' + ''.join(result_find) + '\"'
print(result_find)
print(output)
