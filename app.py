from flask import Flask
app = Flask(__name__)

@app.route('/')
def openCid():
    return 'cdi_app'