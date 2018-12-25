''' This program explores all the synonyms/ context of a word'''

from nltk.corpus import wordnet as wn

table = 'table'

table_synsets = wn.synsets(table)

for current_syn in table_synsets:
    print(current_syn,':')
    print('Definition:', current_syn.definition())
    print('Lemma/ Synchronous words:', current_syn.lemma_names())
    print('Example: ', current_syn.examples(), '\n')
