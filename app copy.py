#1. import Flask
from flask import Flask
#2. Create an app, being sure to pass __name__ in the app variable - we are putting the flask object into the app variable
app = Flask(__name__)

#3. Define what to do when a user hits the index route - in this case this is the homepage - this is a static route
@app.route('/')
def hello_world():
    return "Hello world"