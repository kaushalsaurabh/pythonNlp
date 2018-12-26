'''This program will read text from word'''
import docx


# Function to read text from dox
def get_text_from_word (filename):

    # Load the doc object with document to be read
    print('filename='+filename)
    doc = docx.Document(filename)

    # Read the doc para by para
    text = []
    for para in doc.paragraphs:
        text.append(para.text)

    return '\n'.join(text)

def get_attributes(filename):
    doc = docx.Document(filename)
    print('Number of paragraphs', len(doc.paragraphs))
    print('Second Paragraph', doc.paragraphs[1].text)
    print('Second Paragraph style', doc.paragraphs[1].style)


print(get_attributes('sample_docx_1page.docx'))
