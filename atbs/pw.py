#! python3
# pw.py - an insecure password locker program

passwords = {'email': 'asdfas7fa76sdf6asdf67',
             'blog': 'asdfasdgiiiwrweinr',
             'blahblah': 'dsfkhjdsfkjhasfdjkhasdfkjh'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account)