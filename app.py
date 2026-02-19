
# import all libraries
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Flask Project on AWS"

@app.route('/new')
def new():
    return "Hello world I'm running my project CI"



if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
