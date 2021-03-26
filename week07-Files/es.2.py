
filename = "moby-dick.txt"

import collections
import string

def count_letters(filename, case_sensitive=False):
    with open(filename, 'r') as f:
        original_text = f.read()
    if case_sensitive:
        alphabet = string.ascii_letters
        text = original_text
    else:
        alphabet = string.ascii_lowercase
        text = original_text.lower()
        alphabet_set = set(alphabet)
        counts = collections.Counter(c for c in text if c in alphabet_set)

    for letter in alphabet:
        print(letter, counts[letter])

    print("total:", sum(counts.values()))

    return counts

# count_letters("example.txt")
