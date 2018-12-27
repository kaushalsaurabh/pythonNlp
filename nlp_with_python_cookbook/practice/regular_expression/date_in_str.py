''' This program finds date in string'''
import re

url= "http://www.telegraph.co.uk/formula-1/2017/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewis1/"

''' The date_regex is also a simple string object but it contains a regex that will match a date 
with format YYYY/DD/MM or YYYY/MM/DD type of dates. \d denotes digits starting from 0 to 9 '''
date_regex = '/(\d{4})/(\d{1,2})/(\d{1,2})/'

print("Date found in the URL :", re.findall(date_regex, url))

'''The [] notation that is set essentially means: match either of the characters enclosed inside the set notation.
 If any single match is found, the pattern is true. '''
def is_allowed_specific_char(string):
  charRe = re.compile(r'[^a-zA-Z0-9.]')
  string = charRe.search(string)
  return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450."))
print(is_allowed_specific_char("*&%@#!}{"))