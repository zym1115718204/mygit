#!/usr/bin/pyhton
# Filename: objvar.py

class Person:
    '''Represents a person'''
    #population是一个类的变量
    population=0

    #name变量属于对象（它使用self赋值）因此是对象的变量
    def __init__(self,name):
        '''Initialize the person's data.'''
        self.name=name
        print '(Initializing %s)' %self.name

        #When this person is created,he/she
        #adds to the population
        Person.population += 1

    def __def__(self):
        '''I am dying.'''
        print '%s says bye.'%self.name

        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.'%Person.population
    def sayHi(self):
        '''Greeting by the person.

        Really,that's all it does.'''
        print 'Hi,my name is %s.'%self.name
    def howMany(self):
        '''Prints the current population.'''
        if Person.population ==1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.'%Person.population

swaroop=Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam=Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

#附加的设计1，输入添加新name
#comment=raw_input('Enter a name:')
#p=Person(comment)
#p.sayHi()
#p.howMany()

#附加的设计2，循环输入添加新name，使用quit退出循环程序
running=True
while running:
    comment=raw_input('Enter a new name:')
    if comment!='quit':
        p=Person(comment)
        p.sayHi()跑
        p.howMany()
    else:
        print'The system is over.'
        running=False
print'Done'
    




