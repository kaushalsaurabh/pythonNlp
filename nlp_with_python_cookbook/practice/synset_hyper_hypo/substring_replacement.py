''' This program will perform substring and replace operations'''

str = 'NLTK Dolly Python'

#Substring from start
print(str[:4])

#Substring from to
print(str[5:10])

#Substring Backwards
print(str[-6:-1])

# if operator
if 'NLTK' in str:
  print('found NLTK')

# Replace String
replaced = str.replace('Dolly', 'Dorothy')
print(replaced)

# Accessing each character
for s in replaced:
    print(s)