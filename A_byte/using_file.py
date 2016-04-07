#!/usr/bin/pyhton
# Filename: using_file.py

poem ='''\
Programing is fun
When the work is done
if you wanna make your work also fun:
use python!
'''

#将poem的内容写入txt文件

f=file('poem.txt','w')#open for 'w'riting
f.write(poem)#write text to file
f.close()#close the file

#将poem.txt的内容逐行读出并输出

f=file('poem.txt')
#if no mode is specified,'r'ead mode is assumed by defult

while True:
    line= f.readline()
    if len(line) ==0:
        break
    print line, #默认每一行会换行，使用','进行消除默认换行操作
f.close()
