#
# Send a spoofed email.  Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@gmail.com
# Recipient needs to be zultron@thebigeye.com
#
import smtplib


port = 1025  # For SSL
server = "127.0.0.1"
sender = "bob-roswell-1947@gmail.com"
receiver = "zultron@thebigeye.com"
message = "yeeter skeeter"

try:
  smtpObj = smtplib.SMTP('127.0.0.1', 1025)
  smtpObj.sendmail(sender, receiver, message)
  print "Successfully sent email"
except SMTPException:
  print "Error: unable to send email"