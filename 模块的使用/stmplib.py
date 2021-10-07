import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''
测试邮件发送的流程，需要注意的事项
1、第三方服务的账号密码设置
2、发送邮件时会被定义为垃圾邮件

'''

# 设置邮件发送者的地址，域名
sender = '1048938804@qq.com'
# 接受者的地址
receivers = ['1048938804@qq.com', 'dzw2020@163.com']

# 三个参数，第一个为文本内容，第二个为plain设置文本格式，第三个设置utf-8编码

message = MIMEText('aaa', 'plain', 'utf-8')
message['From'] = Header('bbb', 'utf-8')
message['To'] = Header('aaa', 'utf-8')

# 设置发送内容，主题
subject = 'ttt'
message['Subject'] = Header(subject, 'utf-8')

# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_user = '1048938804@qq.com'
mail_pass = 'mfgcdjeaegzgbfed'
# QQ端：mfgcdjeaegzgbfed
# 163端：RLGNFFKQLIYXLASR

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 发送服务器的端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')
