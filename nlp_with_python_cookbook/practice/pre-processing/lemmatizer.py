'''A lemma is a lexicon headword or, more simply, the base form of a word
A lemma is a dictionary-matched base form unlike the stem obtained by removing/replacing the suffixes'''

from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

# Tokenize the words
raw = "My name is Maximus Decimus Meridius, commander of the armies of the north, General of the Felix legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)
print ('Tokens:', tokens)

# Applying porter stemmer
porter = PorterStemmer()
pstems = [porter.stem(t) for t in tokens]
print('Stems', pstems)

# Applying lemmatizer
lemmatizer = WordNetLemmatizer()
lemmas =[lemmatizer.lemmatize(t) for t in tokens]
print('Lemmas:', lemmas)

