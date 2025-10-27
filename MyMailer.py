import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendMail(from_addr, to_addr, subject, content, files=[]):
    content_type='plain'
    username='cody634455@gmail.com'
    password='dwse mkxb bhvh jtcj'
    smtp='smtp.gmail.com'
    port=587
    msg=MIMEMultipart()
    msg['Subject']=subject
    msg['From']=from_addr
    msg['To']=to_addr
    msg.attach(MIMEText(content, content_type))
    if files:
        for file_item in files:
            if os.path.exists(file_item):
                with open(file_item, 'rb') as f:
                    basename=os.path.basename(file_item)
                    part=MIMEApplication(f.read(),Name=basename)
                    part['Content-Disposition']='attachment; filename="%s"' %basename
                    msg.attach(part)
                    print(basename,'(이)가 첨부되었습니다.')
    mail=SMTP(smtp)
    mail.ehlo()
    mail.starttls()
    mail.login(username,password)
    mail.sendmail(from_addr,to_addr,msg.as_string())
    mail.quit()

if __name__=="__main__":
    sendMail('cody634455@gmail.com','cody6344@naver.com','메일 발송 모듈 테스트','이것은 테스트 입니다.')