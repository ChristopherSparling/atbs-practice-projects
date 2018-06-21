import re

def strip_re (text, remove=''):
    # Default behaviour
    if remove == '':
        chars = re.compile(r'^[\s]*|[\s]*$') 
        text = chars.sub('',text)
        print(text)
    else:
        re_string = r"[" + re.escape(str(remove)) + r"]"
        chars = re.compile(re_string)
        #print(chars)
        text = chars.sub('',text)
        print(re_string)
        print(text)
text = '        asdfafjasdfasfd asdfasdfasdf        '
strip_re(text, 'asd')