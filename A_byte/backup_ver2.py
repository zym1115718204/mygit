#!/usr/bin/python
# Filename:backup_ver2.py

import os
import time

#ȷ����Ҫѹ����Դ�ļ�/Ŀ¼��Ŀ��Ŀ¼
source=r'D:\Python27\example\backup'
target_dir=r'D:\Python27\example\backup2\\'

#��ȡʵʱʱ�����
today=target_dir+time.strftime('%Y-%m-%d')
now=time.strftime('%H%M%S')

#os.sep�Ǹ���ϵͳ����Ŀ¼�ָ�����Linux/Unix��'\'��Window����'\\',Mac OS��':'

#�����ж��Ƿ����������Ϊ���Ƶ�Ŀ¼
if not os.path.exists(today):
    os.mkdir(today)
    print'Successfully created directory'

#��ԭĿ��Ŀ¼����Ϊ·�����ļ���
target=today+os.sep+'Ver2-'+now+'.rar'

#������Ŀ����������rar�ļ�������Դ�ļ�������ļ��У�������������
rar_command='rar a %s %s'%(target,''.join(source))
if os.system(rar_command)==0:
    print'Successful backup to',target
else:
    print'Backup FAILED'

#��ע��
#������Ĵ�����Щ�鵵�ķ����Ƿֱ�ʹ��zipfile��tarfile��
#������Python��׼���һ���֣����Թ���ʹ�á�ʹ����Щ��ͱ�����ʹ��os.system������Ƽ�ʹ�õĺ�����
#�������������صĴ���Ȼ�������ڱ�����ʹ��os.system�ķ������������ݣ��ⴿ����Ϊ�˽�ѧ����Ҫ��
#�����Ļ������ӾͿ��Լ򵥵���ÿ���˶��ܹ���⣬ͬʱҲ�Ѿ��㹻���ˡ�
