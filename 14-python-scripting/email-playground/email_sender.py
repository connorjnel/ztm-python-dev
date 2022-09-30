import smtplib as smtp
import smtplib
from email.message import EmailMessage


connection = smtp.SMTP_SSL('smtp.gmail.com', 465)

email_addr = 'neljovan88@gmail.com'
email_passwd = ''
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr,
                    to_addrs='recipient@something.com', msg="Sent from my IDE. Hehe")
connection.close()
