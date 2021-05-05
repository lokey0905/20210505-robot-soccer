from flask import Flask, render_template
from botControl import run_ActionGroup

app = Flask(__name__)


@app.route("/")
def index():
    run_ActionGroup('0',1)
    return render_template('hyperlink.html')

@app.route("/on")
def On():
    run_ActionGroup('123',1)
    return render_template('hyperlink.html')

@app.route("/off")
def Off():
    run_ActionGroup('0',1)
    return render_template('hyperlink.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
