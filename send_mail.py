import smtplib


def send_mail():
    content = "Hello World"
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = 'fudothedev@gmail.com'
    recipient = 'fudothedev+1@gmail.com'
    # login with gmail, use app password instead of actual password
    # https://stackoverflow.com/a/75096574/8962929
    mail.login('fudothedev@gmail.com', 'xmyi yqpi yvqi ftbj')
    header = 'To:' + recipient + '\n' + 'From:' \
             + sender + '\n' + 'subject:testmail\n'
    content = header + content
    mail.sendmail(sender, recipient, content)
    mail.close()
