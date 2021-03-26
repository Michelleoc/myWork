# send an testEmail
# Author Michelle O'Connor

import smtplib
print ("in testEmail")

username = 'michelleoconnormurphy@gmail.com'
password = 'REMOVED'
toEmail = 'G00398975@gmit.ie'
message = 'Hi there - testing sending an email via python'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(username, toEmail, message)