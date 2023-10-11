"""
https://www.tutorialspoint.com/python/python_sending_email.htm
"""

import smtplib

"""
send email to local server

enable smtp local server
python3 -m smtpd -c DebuggingServer -n localhost:1025
"""
# fromaddr = "test@test.com"
# toaddrs = "test+1@test.com"
# msg = "Hello World"
# server = smtplib.SMTP('localhost', 1025)
# server.set_debuglevel(1)
# server.sendmail(fromaddr, toaddrs, msg)
# server.quit()


"""
send email to actual gmail
"""
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
