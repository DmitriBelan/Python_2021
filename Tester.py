import re

text_to_search = '''
123123123
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
-23*555*5555
800-555-1234
900-555-1234
988-555-2312
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr. O`Rilley
abc

ball mall hall wall tall
333-333-3333333333
'''

sentence = 'Start a sentence Start and then bring it to an+ end bring Start'

pattern = re.compile(r'[a-zA-Z]$')
matches = pattern.findall(text_to_search)
print(matches)
