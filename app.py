import kronos
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from flask import Flask


def send_question():
    print "trying to send a question"
    f = open('prob_num.txt', 'r+')
    num = int(f.read())
    ImgFileName = "coding_images/" + str(num) + ".png" 
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Programming question #{}'.format(num)

    fromaddr = 'programmingquestions1@gmail.com'
    toaddrs = 'lukasfroehlich1@gmail.com'
    msg['From'] = fromaddr
    msg['To'] = toaddrs

    text = MIMEText("programming!!")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("programmingquestions1","Coding123")

    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

    if num >= 92:
        num = -1
    f.seek(0)
    f.write(str(num+1))
    f.close()



sched = kronos.ThreadedScheduler()

sched.add_single_task(action=send_question,
                      taskname="send_quesion",
                      initialdelay=10,
                      processmethod=kronos.method.threaded,
                      args=None,
                      kw=None)

time.sleep(20)
#ksched.add_daytime_task(action=send_question,
#k                       taskname="send_quesion",
#k                       weekdays=[1,2,3,4,5,6,7],
#k                       monthdays=None,
#k                       timeonday=[1,22],
#k                       processmethod=kronos.method.threaded,
#k                       args=None,
#k                       kw=None)

