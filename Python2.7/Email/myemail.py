#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib

#set msg content
msg= MIMEText('Hello,Send by Python...','plain','utf-8')

from_addr = raw_input('From:')
password = raw_input('Password:')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
