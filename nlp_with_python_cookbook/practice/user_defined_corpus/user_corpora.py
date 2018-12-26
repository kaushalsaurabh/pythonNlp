'''This program will create a user defined corpora from a text file, a word file and a pdf file'''

import read_word,read_pdf
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

# Read text from text file
def get_text_from_file (text_file_name):
    file = open(text_file_name, 'r')
    return file.read()

# Create a directory to hold corpus
newCorpusDir = 'mycorpus/'
if not os.path.isdir(newCorpusDir):
  os.mkdir(newCorpusDir)

# Read files word, pdf and text one by one
text_file = get_text_from_file('./samples/sample_feed.txt')
text_word = read_word.get_text_from_word('./samples/sample_docx_1page.docx')
text_pdf = read_pdf.get_text_from_pdf('./samples/sample_pdf_file.pdf')

# Write the text in corpus read from the above files
text = [text_file, text_word, text_pdf]
for idx, f in enumerate(text):
    with open(newCorpusDir + str(idx) + '.txt', 'w') as fout:
        fout.write(f)

# Create plain text corpus object from newCorpusDir
newCorpus = PlaintextCorpusReader(newCorpusDir, '.*')

# Check the words in corpus
print(newCorpus.words())

# Check the sentences in file 1.txt
print(newCorpus.sents(newCorpus.fileids()[1]))

# Check the paragraphs in file 0.txt
print(newCorpus.paras(newCorpus.fileids()[0]))