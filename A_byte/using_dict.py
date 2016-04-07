#!/usr/bin/python
# Filename:using_dict.py

#'ab' is short for 'a'ddress'b'ook

ab={'Swaroop':'swaroopch@byteofpython.info',
    'Larrt':'larry@wall.org',
    'Matsumto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmall.com'
    }

print"Swaroop's address is %s"%ab['Swaroop']
#Adding a key/value pair
ab['Guido']='guido@pyhton.org'
#Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n'%len(ab)
for name,address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Guido' in ab:
    print"\nGuido's address is %s"%ab['Guido']
