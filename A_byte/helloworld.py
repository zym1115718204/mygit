#!/usr/bin/python
#Filename : helloworld.py


#---------------------------------------------------------------------------------------------
print'----------------------��һ���ǵ�һ��Python����--------------------------'
print'Hello World','aaaaa'

i=5
print i
i=i+1
print i

s='''This is a multi-line string.
This is a the second line'''
print s

length=5
breadth=2
area =length*breadth
print 'Area is',area
print 'Perimeter is',2*(length+breadth)

#---------------------------------------------------------------------------------------------
#if �������ʹ��

print'--------------------��һ���ǲ���if�������ʹ��-------------------------'

number=23
guess=int(raw_input('Enter an integer:'))
if guess==number:
    print'Congratulations,you guess it!'#new block starts here
    print'but you do not win any prizes!'#new block end here
elif guess<number:
    print'No, it is a little higher than that'#Another block
    #You can do whatever you want in a block...
elif guess>number:
    print'No, it is a little lower than that'
    #You must have guess>number to reach here
print'done'
# This last statement is always executed, after the if statement is executed

#---------------------------------------------------------------------------------------------
#While �������ʹ��

print'--------------------��һ���ǲ���while�������ʹ��--------------------'

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.' 
        running = False # this causes the while loop to stop
    elif guess < number:
        print 'No, it is a little higher than that' 
    else:
        print 'No, it is a little lower than that' 
else:
    print 'The while loop is over.' 
    # Do anything else you want to do here

print 'Done'

#---------------------------------------------------------------------------------------------
#for��ʹ��

print'-------------------��һ���ǲ���forѭ������ʹ��------------------------'

for i in range(1,5):
    print i
else:
    print'The for loop is over'
#---------------------------------------------------------------------------------------------
#break��ʹ��

print'---------------------��һ���ǲ���break����ʹ��--------------------------'

while True:
    s = raw_input('Enter something:')
    if s=='quit':
        break
    print 'Length of the string is:',len(s)
print'done'

#---------------------------------------------------------------------------------------------
#continue��ʹ��

print'---------------------��һ���ǲ���continue����ʹ��-------------------------'

while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print'Input is of sufficient length'
print'done'   


#---------------------------------------------------------------------------------------------
#ʹ�ú����β�
#---------------------------------------------------------------------------------------------
#ʹ��DocStrings

def printMax(x,y):
    '''Prints the maximum of two numbers.

    The two values must be ingegers.'''
    x=int(x)
    y=int(y)

    if x>y:
        print x,'is maximum'
    else:
        print y,'is maximum'

printMax(3,5)
print printMax.__doc__


























