#!/usr/bin/python
# Filename:backup_ver2.py

import os
import time

#确定需要压缩的源文件/目录及目标目录
source=r'D:\Python27\example\backup'
target_dir=r'D:\Python27\example\backup2\\'

#获取实时时间参数
today=target_dir+time.strftime('%Y-%m-%d')
now=time.strftime('%H%M%S')

#os.sep是根据系统给出目录分隔符，Linux/Unix是'\'，Window下是'\\',Mac OS是':'

#事先判断是否存在以日期为名称的目录
if not os.path.exists(today):
    os.mkdir(today)
    print'Successfully created directory'

#将原目标目录更新为路径及文件名
target=today+os.sep+'Ver2-'+now+'.rar'

#创建以目标名命名的rar文件，并将源文件添加入文件中，并输出创建结果
rar_command='rar a %s %s'%(target,''.join(source))
if os.system(rar_command)==0:
    print'Successful backup to',target
else:
    print'Backup FAILED'

#备注：
#最理想的创建这些归档的方法是分别使用zipfile和tarfile。
#它们是Python标准库的一部分，可以供你使用。使用这些库就避免了使用os.system这个不推荐使用的函数，
#它容易引发严重的错误。然而，我在本节中使用os.system的方法来创建备份，这纯粹是为了教学的需要。
#这样的话，例子就可以简单到让每个人都能够理解，同时也已经足够用了。
