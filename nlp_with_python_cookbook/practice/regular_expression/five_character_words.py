''' This is a program to find all 5 character words'''

import re

# Replace Road with rd for string = street
street = '21 Ramkrishna Road'
print(re.sub('Road', 'Rd', street))

''' \b boundary set to identify the boundary between words and
 the {} notation to make sure we are only shortlisting five-character words '''
text = 'Diwali is a festival of light, Holi is a festival of color!'
print(re.findall(r"\b\w{5}\b", text))

