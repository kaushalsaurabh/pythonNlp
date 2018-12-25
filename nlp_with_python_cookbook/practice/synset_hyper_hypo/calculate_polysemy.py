''' This program calculates average senses of a particular form such as Noun exists in all the senses '''
from nltk.corpus import wordnet as wn
type = 'n'

synsets = wn.all_synsets(type)


lemmas = []
for synset in synsets:
  for lemma in synset.lemmas():
    lemmas.append(lemma.name())

lemmas = set(lemmas)

count = 0
for lemma in lemmas:
  count = count + len(wn.synsets(lemma, type))

print('Total distinct lemmas: ', len(lemmas))
print('Total senses :',count)
print('Average Polysemy of ', type,': ' , count/len(lemmas))