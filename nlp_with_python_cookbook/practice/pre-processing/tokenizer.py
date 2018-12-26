''' This program will create tokens. Tokens can be anything ranging from words, sentence or line'''

from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

# Tokenize Based on line
lTokenizer = LineTokenizer()
print("Line tokenizer output :",lTokenizer.tokenize("My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurelius. \nFather to a murdered son, husband to a murdered wife. \nAnd I will have my vengeance, in this life or the next."))

# Tokenize based on space
sTokenizer = SpaceTokenizer()
rawText = "By 11 o'clock on Sunday, the doctor shall open the dispensary."
print('Space Tokenizer:', sTokenizer.tokenize(rawText))

# Tokenize based on words
print("Word Tokenizer output :", word_tokenize(rawText))

# Tweets contain special words, special characters, hashtags, and smileys that we want to keep intact. Tokenize based on tweets
tTokenizer = TweetTokenizer()
print("Tweet Tokenizer output :", tTokenizer.tokenize("This is a cooool #dummysmiley: :-) :-P <3"))