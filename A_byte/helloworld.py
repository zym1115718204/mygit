#!/usr/bin/python
#Filename : helloworld.py


#---------------------------------------------------------------------------------------------
print'----------------------这一段是第一个Python程序--------------------------'
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
#if 条件句的使用

print'--------------------这一段是测试if条件句的使用-------------------------'

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
#While 条件句的使用

print'--------------------这一段是测试while条件句的使用--------------------'

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
#for的使用

print'-------------------这一段是测试for循环语句的使用------------------------'

for i in range(1,5):
    print i
else:
    print'The for loop is over'
#---------------------------------------------------------------------------------------------
#break的使用

print'---------------------这一段是测试break语句的使用--------------------------'

while True:
    s = raw_input('Enter something:')
    if s=='quit':
        break
    print 'Length of the string is:',len(s)
print'done'

#---------------------------------------------------------------------------------------------
#continue的使用

print'---------------------这一段是测试continue语句的使用-------------------------'

while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print'Input is of sufficient length'
print'done'   


#---------------------------------------------------------------------------------------------
#使用函数形参
#---------------------------------------------------------------------------------------------
#使用DocStrings

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


























