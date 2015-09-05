import kronos
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class qScheduler():

    def send_test_email():
        fromaddr = 'programmingquestions1@gmail.com'
        toaddrs = 'lukasfroehlich1@gmail.com'
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login("programmingquestions1","Coding123")

        server.sendmail(fromaddr, toaddrs, "yoooooo")
        server.quit()


    sched = kronos.ThreadedScheduler()
    sched.start()
    print "scheduler created"

    sched.add_single_task(action=send_test_email,
                          taskname="testoutput",
                          initialdelay=1,
                          processmethod=kronos.method.threaded,
                          args=None,
                          kw=None)

sched = qScheduler()
