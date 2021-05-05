from flask import Flask, render_template
from botControl import run_ActionGroup

app = Flask(__name__)


@app.route("/")
def index():
    run_ActionGroup('0',1)
    return render_template('wave_off.html')

@app.route("/on")
def LED_On():
    run_ActionGroup('123',1)
    return render_template('wave_on.html')

@app.route("/off")
def LED_Off():
    run_ActionGroup('0',1)
    return render_template('wave_off.html')

if __name__ == "__main__":
    app.run()
    
    
    
    
    
    
    
    
    
