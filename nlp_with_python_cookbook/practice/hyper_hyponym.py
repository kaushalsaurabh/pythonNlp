''' This program is used to find hypernym and hyponym and get the complete path'''

from nltk.corpus import wordnet as wn

woman = wn.synset('woman.n.02')
bed = wn.synset('bed.n.01')

######### Hypernym #################
print(woman.hypernyms())
woman_paths = woman.hypernym_paths()
print(woman_paths[1])


# There might be more than one path leading to woman
for idx, path in enumerate(woman_paths):
  print('\n\nHypernym Path :', idx + 1)
  for synset in path:
    print(synset.name(), ', ', end='')

######### Hyponym ####################
types_of_beds = bed.hyponyms()
print('\n\nTypes of beds(Hyponyms): ', types_of_beds)

# Print names in sorted order
for synset in types_of_beds:
    print(synset.name(),', ', end='')

print('Sorted')
print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))
