import shutil, os,re

datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """,re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None: continue

    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)

    euroFilename = before  + day + '-' + month + '-' + year + after

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename,euroFilename))
    shutil.move(amerFilename, euroFilename)