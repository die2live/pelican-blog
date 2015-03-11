Title: Sending emails with attachments via Gmail with Python
Date: 2014-04-08 09:16
Author: dai
Category: Tips
Tags: attachment, email, gmail, python, send email
Slug: sending-emails-with-attachments-via-gmail-with-python

    #!/usr/bin/python

    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email.MIMEText import MIMEText
    from email import Encoders
    import os

    gmail_user = "your_email@gmail.com"
    gmail_pwd = "your_password"

    def mail(to, subject, text, attach):
    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',  'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()

    mail("some.person@some.address.com",
    "Hello from python!",
    "This is a email sent with python",
    "my_picture.jpg")
