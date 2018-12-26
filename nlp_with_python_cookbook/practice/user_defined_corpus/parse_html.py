''' This program will Parse HTML using BeautifulSoup - content, tag and attributes
pip install beautifulsoup4 '''

from bs4 import BeautifulSoup

# Read HTML doc
html_doc = open('./samples/sample-html.html', 'r').read()
soup = BeautifulSoup(html_doc, 'html.parser')

# Get only the content - strip tags
print('Full text HTML Stripped:', soup.get_text())

# Get only the HTML stripped text from <h1> tag now
print('Accessing the text of <H1> tag :', end=' ')
print(soup.h1.string)

# Access the alt attribute of the img tag
print('Accessing alt attribute of image tag:', soup.img['alt'])

# Find all the p tags
print('Finding all the occurences of <p> tag:')
for p in soup.find_all('p'):
    print(p.string)

