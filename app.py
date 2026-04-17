import flask 
import os
from datetime import datetime
app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')
@app.route('/status')
def status():
    user = os.popen("whoami").read().strip()
    hostname = os.popen("hostname").read().strip()
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")

    return flask.render_template('status.html', user=user, hostname=hostname, datetime=now_str)
app.run(host="0.0.0.0", port=5000) 