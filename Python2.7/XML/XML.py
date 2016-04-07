#!/user/bin/python
# -*- coding: utf-8 -*-
#filename:XML

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s, atters:%s'%(name,str(attrs)))

    def end_element(self,name):
        print('sax:end_element:%s' %name)

    def char_data(self,text):
        print('sax:char_data:%s' %text)

xml = r'''<?xml version="1.0"?><ol><li><a href="/python">Python</a></li><li><a href="/ruby">Ruby</a></li></ol>'''

#with open('xml1.xml','w+') as f:
    #f.write(xml)
    #print 'file write ok!\n'

with open('xml.xml','r') as f:
    xmldata=f.read()
    print 'file read ok!\n'

def read_xml():
    try:
        handler=DefaultSaxHandler()
        parser=ParserCreate()
        parser.returns_unicode = True
        parser.StartElementHandler = handler.start_element
        parser.EndElementHandler = handler.end_element
        parser.CharacterDataHandler = handler.char_data

        parser.Parse(xmldata)
    except:
        print 'read error!'
    
read_xml()

