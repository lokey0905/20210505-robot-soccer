from flask import Flask, request, make_response,render_template
import json
from botControl import run_ActionGroup

app = Flask(__name__)

def forward():
   run_ActionGroup('1',1)

def stop():
    run_ActionGroup('0',1)

def backward():
    run_ActionGroup('2',1)  

def right():
    run_ActionGroup('4',1)

def left():
    run_ActionGroup('3',1)

@app.route('/test', methods=['POST'])
def index():
    carCmd = {'f':forward,'l': left,'r':right,'b':backward,'s':stop}
    returnText = {'f':'前進','l':'左轉','r':'右轉','b':'後退','s':'停止'} 
    data = request.form['message']
    if data in carCmd:
        carCmd[data]()
        return '目前行進方向：' + returnText[data]
    return '???'

@app.route('/')
def main():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")