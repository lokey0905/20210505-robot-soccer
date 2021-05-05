from flask import Flask ,request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    text = request.args.get('username')
    return render_template('PlayRobot.html',user_template = text)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
