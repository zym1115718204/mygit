#!/usr/bin/python
# Filename:backup_ver3.py

#����⺯��
import os
import time

#ȷ����Ҫѹ����Դ�ļ�/Ŀ¼�Լ������Ŀ��Ŀ¼
source=r'D:\Python27\example\backup'
target_dir=r'D:\Python27\example\backup2\\'

#��ȡ��Ҫʹ��ʱ�����
today=target_dir+time.strftime('%Y-%m-%d')
now=time.strftime('%H%M%S')

#�����ļ�ǰ���������,��ԭĿ��Ŀ¼����Ϊ·�����ļ���
comment=raw_input('Enter a comment -->')
if len(comment)==0:
    target=today+os.sep+'Ver3-'+now+'.rar'
else:
    target=today+os.sep+'Ver3-'+now+'_'+comment.replace(' ','_')+'.rar'
    #������һ���� �����м京�пո񣬷��򴴽����ļ�����������abc����a_b_c��

#Ԥ���ж�ʱ��Ŀ¼�Ƿ���ڣ����򴴽�Ŀ¼�ļ�
if not os.path.exists(today):
    os.mkdir(today)
else:
    print'Successfully created directory'

#������Ŀ����������rar�ļ�������Դ�ļ�/Ŀ¼��ӽ�rar�ļ��У�������������
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


    
