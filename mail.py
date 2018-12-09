
import smtplib

def sendGmail(senderId, pwd, receiverId, msg):
 server=smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(senderId,pwd)
 server.sendmail(senderId,receiverId,msg)
 server.quit()
