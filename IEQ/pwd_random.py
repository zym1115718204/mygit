#!/usr/bin/python
# Filename:pwd_random.py

#不调用函数类型的方法
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

#以函数调用的形式的方法
def _random_passwd(self,randomlength=8):
        from random import Random
        pwd = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            pwd+=a+chars[random.randint(0, length)]
            #这里是用来展示pwd的生成过程
            #print pwd
        return pwd
    
#_random_passwd()需要定义一个参数，我们任意定义一个a='%',a=''等等    
a=''

#我们将a参数，传入函数中，函数中可以用a也可以不用,还可以传入参数如randomlength=10等
print 'NewPassword="%s"' %_random_passwd(a)
p=_random_passwd(a,randomlength=10)  
print 'NewPassword="%s"' %p

#函数调用完毕后，a本身不会发生变化   
print a
