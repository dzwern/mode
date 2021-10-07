import itertools
import logging
import mimetypes
import smtplib
import traceback

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class ZsMail(object):
    def sendMail(self, mail_msg="", attachFile="", subject="", sender="reporting@mx2.zzss.com",
                 receiver=None,cc=None):

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ",".join(itertools.chain(receiver))

        if cc is not None:
            if isinstance(cc,list):
                message['Cc'] = ",".join(itertools.chain(cc))
            else:
                raise ValueError("cc should be a list")
        else:
            cc = []

        if receiver is None:
            all_receiver = ['dongweifeng@mx2.zzss.com']

        elif not isinstance(receiver,list):
            all_receiver = [receiver] + cc
        else:
            all_receiver = receiver + cc

        message['Subject'] = subject

        # 邮件正文内容(Html页面展示文件内容)
        message.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 遍历attachFile   (需要逗号分隔)
        if attachFile.strip():
            filelist = attachFile.split(",")
            for i in range(len(filelist)):
                singleFile = filelist[i].strip()

                ctype, encoding = mimetypes.guess_type(singleFile)
                if ctype is None or encoding is not None:
                    ctype = "application/octet-stream"

                maintype, subtype = ctype.split("/", 1)

                if maintype == "text":
                    fp = open(singleFile)
                    attachment = MIMEText(fp.read(), _subtype=subtype)
                    fp.close()
                elif maintype == "image":
                    fp = open(singleFile, "rb")
                    attachment = MIMEImage(fp.read(), _subtype=subtype)
                    fp.close()
                elif maintype == "audio":
                    fp = open(singleFile, "rb")
                    attachment = MIMEAudio(fp.read(), _subtype=subtype)
                    fp.close()
                else:
                    fp = open(singleFile, "rb")
                    attachment = MIMEBase(maintype, subtype)
                    attachment.set_payload(fp.read())
                    fp.close()
                    encoders.encode_base64(attachment)

                attachment.add_header("Content-Disposition", "attachment",
                                      filename=("gbk", "", singleFile.split("/")[-1]))
                message.attach(attachment)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(host="mx2.zzss.com", port=25)  # 25 为 SMTP 端口号
            smtpObj.login(user="reporting@mx2.zzss.com", password="QUNArp123")
            smtpObj.sendmail(from_addr=sender, to_addrs=all_receiver, msg=message.as_string())
            flag = "邮件发送成功……..."
        except:
            flag = "Error:无法发送邮件！！！"
            logging.error(traceback.format_exc())
        finally:
            logging.info(flag)
