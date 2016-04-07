#!/user/bin/python
# -*- coding: utf-8 -*-
#filename:HTML

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('%s'%data)

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
#with open('html2.htm','r') as f:
with open('FengSensor.html','r') as f:
    html=f.read()
    html2='''<html>i'm head</head><body><p>i'm body
          <a href=\"#\">html</a> i'm tutorial...<br>i'm END</p></body></html>
          '''
parser.feed(html)
print 'OK'
