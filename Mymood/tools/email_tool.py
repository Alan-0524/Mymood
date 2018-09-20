import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.gmail.com"
mail_user = "long.an.0524@gmail.com"
mail_pass = "qwe!@#196385"
sender = 'long.an.0524@gmail.com'
receiver = ['119241066@163.com']

msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')

msg['From'] = Header("测试邮件", 'utf-8')
msg['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
msg['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP(mail_host, 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    # smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receiver, msg.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")
