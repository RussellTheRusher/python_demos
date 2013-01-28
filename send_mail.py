#! /usr/bin/python2.7
# -*- encoding:utf-8 -*-
# vim: set nu ai sw=4 ts=4 tw=79:

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
#from email.header import Header
msg = MIMEText('Python send mail!', 'plain', 'utf-8')
msg['Subject'] = "Russell recieve it"
msg['From'] = 'xiong-lt'
msg['To'] = 'RussellTheRusher@163.com'
msg['Date'] = formatdate(localtime=True)
smtp = smtplib.SMTP("smtp.163.com")
smtp.login("RussellTheRusher", "******")
smtp.sendmail("RussellTheRusher@163.com", "RussellTheRusher@163.com", msg.as_string())
smtp.close()
print msg.as_string()
