#!/usr/bin/python
# Filename:back_ver1.py

import os
import time

#1.The files and directories to be backed up are apecified in a list.
source=r'D:\Python27\example\backup'
source=[r'D:\Python27\example\backup']#另外一种格式
source=[r'D:\Python27\example\backup',]#另外一种格式
#source=[r'D:\Python27\example\backup',r'D:\Python27\example\backup1']#不清楚为什么不可用


#2.The backip must be stored in a main backup directory
#target_dir='D:\\Python27\\example\\backup2\\'
target_dir=r'D:\Python27\example\backup2\\'#两种转义格式都可以用

#3.The files are backed up into a zip file.
#4.The name of zip archive si the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

#5.We use the zip command(in Unix/Linux) to put the files in a zip archive

#Windows下把rar.exe程序添加到system32中，实现cmd中rar命令。并用rar代替zip。
rar_command = 'rar a %s %s'%(target,''.join(source))

#下面这种是Linux自带的zip命令，windows下不可用
#zip_command = 'rar a "%s" %s'%(target,''.join(source))

#Run the backup
if os.system(rar_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup FAILED'

#备注：
#最理想的创建这些归档的方法是分别使用zipfile和tarfile。
#它们是Python标准库的一部分，可以供你使用。使用这些库就避免了使用os.system这个不推荐使用的函数，
#它容易引发严重的错误。然而，我在本节中使用os.system的方法来创建备份，这纯粹是为了教学的需要。
#这样的话，例子就可以简单到让每个人都能够理解，同时也已经足够用了。
