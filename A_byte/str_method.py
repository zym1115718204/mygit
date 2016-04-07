#!/usr/bin/python
# Filename: str_method.py

name='Swaroop'#This is aatring object

if name.startswith('Swar'):
    print 'Yes, the string starts with "Swar"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('war') !=-1:
    print 'Yes, it contains the string "war"'

delimiter='_*_'
mylist =['Brazil','Russia','India','China']
print delimiter.join(mylist)
