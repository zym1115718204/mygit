#!/usr/bin/pyhton
# Filename: using_file.py

poem ='''\
Programing is fun
When the work is done
if you wanna make your work also fun:
use python!
'''

#��poem������д��txt�ļ�

f=file('poem.txt','w')#open for 'w'riting
f.write(poem)#write text to file
f.close()#close the file

#��poem.txt���������ж��������

f=file('poem.txt')
#if no mode is specified,'r'ead mode is assumed by defult

while True:
    line= f.readline()
    if len(line) ==0:
        break
    print line, #Ĭ��ÿһ�лỻ�У�ʹ��','��������Ĭ�ϻ��в���
f.close()
