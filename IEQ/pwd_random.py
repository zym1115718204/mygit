#!/usr/bin/python
# Filename:pwd_random.py

#�����ú������͵ķ���
'''
from random import Random
pwd = ''
randomlength=8
chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
length = len(chars) - 1
random = Random()
for i in range(randomlength):
    pwd+=chars[random.randint(0, length)]
print pwd
'''

#�Ժ������õ���ʽ�ķ���
def _random_passwd(self,randomlength=8):
        from random import Random
        pwd = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            pwd+=a+chars[random.randint(0, length)]
            #����������չʾpwd�����ɹ���
            #print pwd
        return pwd
    
#_random_passwd()��Ҫ����һ���������������ⶨ��һ��a='%',a=''�ȵ�    
a=''

#���ǽ�a���������뺯���У������п�����aҲ���Բ���,�����Դ��������randomlength=10��
print 'NewPassword="%s"' %_random_passwd(a)
p=_random_passwd(a,randomlength=10)  
print 'NewPassword="%s"' %p

#����������Ϻ�a�����ᷢ���仯   
print a
