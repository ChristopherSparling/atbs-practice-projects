import re,sys

checkPassword = re.compile(r'''
^
(?=.*[A-Z])
(?=.*[0-9])       
(?=.*[a-z]) 
.{8,}
$                      
''', re.VERBOSE)

text = str(sys.argv[1])
print(text)
print(checkPassword.search(text).group())