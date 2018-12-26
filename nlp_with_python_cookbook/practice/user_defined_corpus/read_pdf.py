'''This program reads pdf file'''
from PyPDF2 import PdfFileReader
import sys

def get_text_from_pdf (pdf_file_name , password = ''):

    # Initialize pdf file reader
    pdf_file = open (pdf_file_name, 'rb')
    read_pdf = PdfFileReader(pdf_file)

    # Decrypt file with password
    if password != '':
        read_pdf.decrypt()

    # Read the text from pdf pagewise and append
    text = []
    for i in range(0, read_pdf.getNumPages()-1):
        text.append(read_pdf.getPage(i).extractText())

    return '\n'.join(text)

# Call the function with appropriate parameters
#print(get_text_from_pdf("samples/sample_pdf_file.pdf"))



