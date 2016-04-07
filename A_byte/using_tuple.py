#!usr/bin/python
# Filename: using_tuple.py

zoo=('wolf','elephant','penguin')
print 'Number of animals in the zoo is',len(zoo)

new_zoo=('monkey','dolphin',zoo)
print'Number of animals in the new zoo is',len(new_zoo)
print 'All animals in new zoo are',new_zoo
print 'Animals brought form old zoo are',new_zoo[2]
print 'Last animals brought form old zoo is',new_zoo[2][2]

new_zoo2=(new_zoo,)
print 'Number of animals in the zoo is',len(new_zoo2)
print 'All animals of in the new zoo2 are',new_zoo2
print 'Last animals brought form old zoo is',new_zoo2[0][2][2]

new_zoo2.append('miaomiao')#此行会出错，因为元组是不可以修改的！
