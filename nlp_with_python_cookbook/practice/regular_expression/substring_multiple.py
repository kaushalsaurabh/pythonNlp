'''This program will search multiple literal strings or substrings'''

import  re

patterns = [ 'Tuffy', 'Pie', 'Loki' ]
text = 'Tuffy eats pie, Loki eats peas!'

# Search for a word in sentence and find whether it exists or not using for loop
for pattern in patterns:
  print('Searching for "%s" in "%s" -&gt;' % (pattern, text),)
  if re.search(pattern,  text):
    print('Found!')
  else:
    print('Not Found!')

# Search for a substring and find its exact location
text = 'Diwali is a festival of lights, Holi is a festival of colors!'
pattern = 'festival'


'''The finditer function takes as input the pattern and the input text on which to apply that pattern. 
On the returned list, we shall iterate. For every object, we will call the start and
 end methods to know the exact location where we found a match for the pattern'''
for match in re.finditer(pattern, text):
  s = match.start()
  e = match.end()
  print('Found "%s" at %d:%d' % (text[s:e], s, e))

