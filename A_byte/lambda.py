#!/usr/bin/python
# Filename:lambda.py

#ʹ��make_repeater����������ʱ�����µĺ������󣬲��ҷ�����
#lambda������������������󣬱����ϣ�lambda��Ҫһ����������������������ʽ��Ϊ������
#���ʽ��ֵ������½��ĺ�������
#ע�⼴ʹ��print���Ҳ��������lambda�У�ֻ��ʹ�ñ��ʽ
def make_repeater(n):
    return lambda s:s*n

twice=make_repeater(2)
ten=make_repeater(10)

print twice('word')
print twice(2)
print ten('hello!')
print ten(2)

#exec�������ִ�д������ַ��������ļ��е�python���
exec'print"Hello World!"'

#eval��������洢���ַ����е���Чpython���ʽ
#print eval('2*3')

mlt=eval('2*3')
print mlt

