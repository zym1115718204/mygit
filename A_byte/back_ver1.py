#!/usr/bin/python
# Filename:back_ver1.py

import os
import time

#1.The files and directories to be backed up are apecified in a list.
source=r'D:\Python27\example\backup'
source=[r'D:\Python27\example\backup']#����һ�ָ�ʽ
source=[r'D:\Python27\example\backup',]#����һ�ָ�ʽ
#source=[r'D:\Python27\example\backup',r'D:\Python27\example\backup1']#�����Ϊʲô������


#2.The backip must be stored in a main backup directory
#target_dir='D:\\Python27\\example\\backup2\\'
target_dir=r'D:\Python27\example\backup2\\'#����ת���ʽ��������

#3.The files are backed up into a zip file.
#4.The name of zip archive si the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

#5.We use the zip command(in Unix/Linux) to put the files in a zip archive

#Windows�°�rar.exe������ӵ�system32�У�ʵ��cmd��rar�������rar����zip��
rar_command = 'rar a %s %s'%(target,''.join(source))

#����������Linux�Դ���zip���windows�²�����
#zip_command = 'rar a "%s" %s'%(target,''.join(source))

#Run the backup
if os.system(rar_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup FAILED'

#��ע��
#������Ĵ�����Щ�鵵�ķ����Ƿֱ�ʹ��zipfile��tarfile��
#������Python��׼���һ���֣����Թ���ʹ�á�ʹ����Щ��ͱ�����ʹ��os.system������Ƽ�ʹ�õĺ�����
#�������������صĴ���Ȼ�������ڱ�����ʹ��os.system�ķ������������ݣ��ⴿ����Ϊ�˽�ѧ����Ҫ��
#�����Ļ������ӾͿ��Լ򵥵���ÿ���˶��ܹ���⣬ͬʱҲ�Ѿ��㹻���ˡ�
