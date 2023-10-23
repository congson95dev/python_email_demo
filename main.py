"""
https://www.tutorialspoint.com/python/python_sending_email.htm
"""

import smtplib
import redis
from rq import Queue, Connection

from send_mail import send_mail

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
# content = "Hello World"
# mail = smtplib.SMTP('smtp.gmail.com', 587)
# mail.ehlo()
# mail.starttls()
# sender = 'fudothedev@gmail.com'
# recipient = 'fudothedev+1@gmail.com'
# # login with gmail, use app password instead of actual password
# # https://stackoverflow.com/a/75096574/8962929
# mail.login('fudothedev@gmail.com', 'xmyi yqpi yvqi ftbj')
# header = 'To:' + recipient + '\n' + 'From:' \
#          + sender + '\n' + 'subject:testmail\n'
# content = header + content
# mail.sendmail(sender, recipient, content)
# mail.close()


"""
send email to actual gmail with queue (redis)
"""
# url for local redis
redis_url = "redis://localhost:6379"
# url for docker redis
# redis_url = "redis://redis:6379/0"
redis_connection = redis.from_url(redis_url)
with Connection(redis_connection):
    q = Queue()
    q.enqueue(send_mail)  # have to call to function in another file, or error


"""
SES by smtplib, this will require smtp credential to work
https://www.aabidsofi.com/posts/sending-emails-with-aws-ses-and-python/
"""
# from smtplib import SMTP
#
#
# def send_email_with_ses(sender, receiver, message):
#     # getting the credentials fron evironemnt
#     host = "your-aws-host"
#     user = "your-aws-smtp-user"
#     password = "your-aws-smtp-password"
#     port = 587
#
#     # Create the email headers
#     headers = f"From: {sender}\r\nTo: {receiver}\r\nSubject: Test Smtp Email\r\n"
#
#     # Create the email body
#     message = f"{headers}\r\n{message}"
#
#     try:
#         # creating an unsecure smtp connection
#         with SMTP(host, port) as server:
#             # securing using tls
#             server.starttls()
#
#             # authenticating with the server to prove our identity
#             server.login(user=user, password=password)
#
#             # sending a plain text email
#             server.sendmail(sender, receiver, message)
#     except smtplib.SMTPException as e:
#         print(f"An error occurred while sending the email: {e}")
#
#
# send_email_with_ses("your-email@example.com", "your-email+1@example.com",
#                     "hello world")



"""
SES by boto3 (not success, this will require aws credential to make it work)
https://docs.aws.amazon.com/ses/latest/dg/send-an-email-using-sdk-programmatically.html
https://www.learnaws.org/2020/12/18/aws-ses-boto3-guide/
"""
# import boto3
#
# client = boto3.client(
#     'ses',
#     region_name="ap-northeast-1"
# )
#
# response = client.send_email(
#     Destination={
#         'ToAddresses': ["thomas.nguyen1@vmogroup.com"],
#     },
#     Message={
#         'Body': {
#             'Text': {
#                 'Charset': 'UTF-8',
#                 'Data': 'email body string',
#             },
#         },
#         'Subject': {
#             'Charset': 'UTF-8',
#             'Data': 'email subject string',
#         },
#     },
#     Source="lifescience-dev@mlvn-macromil.com",
# )

print("done")
