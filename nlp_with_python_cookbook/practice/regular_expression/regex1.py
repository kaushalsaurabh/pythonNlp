''' This program illustrates the use of regular expressions *, ? , +'''

import re

# Function to do pattern match
def text_match(text, patterns):
    if re.search(patterns, text):
        return 'Match Found'
    else:
        return 'No match found'

# a followed by zero or one b.
print(text_match("ac", "ab?"))
print(text_match("abc", "ab?"))
print(text_match("abbc", "ab?"))

# a followed by zero or more b
print(text_match("ac", "ab*"))
print(text_match("abc", "ab*"))
print(text_match("abbc", "ab*"))

# The one or more wild card
print(text_match("ac", "ab+"))
print(text_match("abc", "ab+"))
print(text_match("abbc", "ab+"))

# a followed by exactly two b
print(text_match("abbc", "ab{2}"))

# a followed by b in range 3 to 5
print(text_match("aabbbbc", "ab{3,5}?"))