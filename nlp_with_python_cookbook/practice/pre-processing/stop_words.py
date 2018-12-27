''' A stopword is a word that, though it has significant syntactic value in sentence formation,
carries very negligible or minimal semantic value. This program will filter stop words'''

import nltk
from nltk.corpus import gutenberg

# Print files
print(gutenberg.fileids())

# Pre-processing step - Filtering words of length >=3
gb_words = gutenberg.words('bible-kjv.txt')
words_filtered = [e for e in gb_words if len(e) >= 3]

# Pre-processing. Stop word treatement
stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words_filtered if w.lower() not in stopwords]

# Calculate Frequency Distribution
fdistPlain = nltk.FreqDist(words)
fdist = nltk.FreqDist(gb_words)

# Statistics about frequency distribution
print('Following are the most common 10 words in the bag')
print(fdistPlain.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdist.most_common(10))
