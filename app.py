
# import all libraries
from flask import Flask

app = Flask(__name__)

@app.route('/new')
def new():
    return "Hello World is Awesome"



if (__name__ == "__main__"):
    app.run(host="0.0.0.0")