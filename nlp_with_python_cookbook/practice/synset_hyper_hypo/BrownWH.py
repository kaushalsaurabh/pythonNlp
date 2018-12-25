''' This program is used to find WH words like WHICH , WHEN in Brown College Campus Corpora.
Categories are already available'''
import nltk
from nltk.corpus import brown

#print(brown.categories())

genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']

for i in range (0, len(genres)):
    genre = genres[i]
    genre_text = brown.words(categories = genre)

fdist = nltk.FreqDist(genre_text)

for frwords in whwords:
    print(frwords + ':', fdist[frwords], end=' ')