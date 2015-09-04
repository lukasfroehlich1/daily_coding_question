from flask import Flask
from scheduler import *

app = Flask(__name__)
print "things are getting started"

if __name__ == '__main__':
    app.run()
