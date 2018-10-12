#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import logging
 
sender = 'monitor@min.com'
revs = ['912279158@qq.com']  # address
 
def sendEmail(body, receivers = revs):
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("monitor", 'utf-8')    # sender
    message['To'] =  Header("reader", 'utf-8')      # receiver
 
    subject = 'check data'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        logging.info(message)
        smtpObj.sendmail(sender, receivers, message.as_string())
        logging.info("mail send succeeded.")
    except smtplib.SMTPException as e:
        logging.error(e)
        logging.error("Error: mail send error")


if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    body = 'zjdr: %s'%('23.1')
    sendEmail(body, revs)  
