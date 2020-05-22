from flask import Flask
from application_setup import ApplicationSetup

app = Flask(__name__)
app.config.from_object(ApplicationSetup().get_config())


@app.route('/')
def hello_world():
    return 'Hello, World!'
