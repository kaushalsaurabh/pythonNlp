''' This program does word analysis and plots word frequency at the end'''

import nltk
from nltk.corpus import webtext


print('Files:',webtext.fileids())

personal_advertising_data_words = webtext.words('singles.txt')
frequency_distribution =  nltk.FreqDist(personal_advertising_data_words)

print('Count of the maximum appearing token "',frequency_distribution.max(),'" : ', frequency_distribution[frequency_distribution.max()])

print('Total number of distinct tokens: ', frequency_distribution.N())

print('Most common words',frequency_distribution.most_common(10))

#print('Tabulate the entire frequency:',frequency_distribution.tabulate())

frequency_distribution.plot(cumulative=True)