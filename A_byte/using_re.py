#!/usr/bin/python
# Filename: using_re.py

import re

line='Cats are smarter than dogs'
#matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
matchObj= re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
#注意正则式中的空格，否则出错

if matchObj:
    print 'matchObj.group():',matchObj.group()
    print 'matchObj.group(1):',matchObj.group(1)
    print 'matchObj.group(2):',matchObj.group(2)
else:
    print 'No match!'
