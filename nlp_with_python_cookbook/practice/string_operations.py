''' This program performs various string operations'''

# Join method
namesList = ['Tuffy','Ali','Nysha','Tim' ]
sentence = 'My dog sleeps on sofa'
names = ';'.join(namesList)
print(type(names), ':', names)

# split method
wordList = sentence.split(' ')
print((type(wordList)), ':', wordList)

# Arithmetic operators + and *
additionExample = 'ganehsa' + 'ganesha' + 'ganesha'
multiplicationExample = 'ganesha' * 2
print('Text Additions :', additionExample)
print('Text Multiplication :', multiplicationExample)