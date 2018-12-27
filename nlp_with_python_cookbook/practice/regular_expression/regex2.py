''' This program will illustrate the use of starts with (^) and ends with ($) operators'''

import re

def text_match (text, pattern):
    if re.search(pattern, text):
        return 'Match Found'
    else:
        return 'No Match Found'

# start with a, followed by zero or more of any characters, and end with c
print("Pattern to test starts and ends with")
print(text_match("abbc", "^a.*c$"))

# pattern that looks for an input text that begins with a word
print("Begin with a word")
print(text_match("Tuffy eats pie, Loki eats peas!", "^\w+"))


'''The pattern means one or more occurrences of \w, followed by zero or more occurrences of \S,
 and that should be falling towards the end of the input text. To understand \S (capital S),
  we must first understand \s, which is all whitespace characters. \S is the reverse or the anti-set of \s,
   which when followed by \w translates to looking for a punctuation:'''
print("End with a word and optional punctuation")
print(text_match("Tuffy eats pie, Loki eats peas!", "\w+\S*?$"))


''' \B is a anti-set or reverse of \b. The \b matches an empty string at the beginning or end of a word,
 and we have already seen what a word is. Hence, \B will match inside the word and 
 it will match any word in our input string that contains character u: '''
print("Finding a word which contains character, not start or end of the word")
print(text_match("Tuffy eats pie, Loki eats peas!", "\Bu\B"))