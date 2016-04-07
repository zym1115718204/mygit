#!/usr/bin/python
# Filename: pickling.py

import cPickle as p
#import Pickle as p

shoplistfile='shoplist.data'
#the name of the file where we will store the object

shoplist=['apple','mango','carrot']

# Write to the file
f=file(shoplistfile,'a')
p.dump(shoplist,f)#dump the object to a file
f.close()

del shoplist #remove the shoplist

#Read back from the storage
f=file(shoplistfile)
storelist=p.load(f)
print storelist
