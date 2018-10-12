#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import logging
 
sender = 'monitor@min.com'
revs = ['912279158@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
def sendEmail(body, receivers = revs):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("monitor", 'utf-8')    # 发送者
    message['To'] =  Header("reader", 'utf-8')      # 接收者
 
    subject = 'check data'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        logging.info(message)
        smtpObj.sendmail(sender, receivers, message.as_string())
        logging.info("邮件发送成功")
    except smtplib.SMTPException as e:
        logging.error(e)
        logging.error("Error: 无法发送邮件")


if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    body = 'zjdr: %s'%('23.1')
    sendEmail(body, revs)  
