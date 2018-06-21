#! python 3
"""
Copy this for input:

Line A
Line B
Line C
Line D
Line E
"""
import pyperclip

lines = pyperclip.paste()
print(lines) 

lines = lines.split('\n')

for index in range(len(lines)):
    lines[index] = '* ' + lines[index]

text = '\n'.join(lines)
pyperclip.copy(text)