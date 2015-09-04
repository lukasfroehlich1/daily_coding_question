from flask import Flask
#from scheduler import *
from test_scheduler import *

app = Flask(__name__)
print "things are getting started"

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()
