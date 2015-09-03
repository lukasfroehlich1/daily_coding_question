from flask import Flask
from scheduler import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

#ksched.add_daytime_task(action=send_question,
#k                       taskname="send_quesion",
#k                       weekdays=[1,2,3,4,5,6,7],
#k                       monthdays=None,
#k                       timeonday=[1,22],
#k                       processmethod=kronos.method.threaded,
#k                       args=None,
#k                       kw=None)

