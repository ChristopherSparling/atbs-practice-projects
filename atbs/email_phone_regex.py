"""
Copy the below text:

chris@gmail.com
jacob@gmail.com
tom@gmail.com
999-999-9999
paul@gmail.com
123-456-7890
"""

import re,pyperclip

# No extensions
phoneRegex = re.compile(r'''(
    (\d{3})|\(\d{3}\))?
    (\s|\.|-)?
    (\d{3})
    (\s|\.|-)
    (\d{4})
    ''',re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copy entries to clipboard: ')
    print('\n'.join(matches))
else:
    print('Nothing Found')