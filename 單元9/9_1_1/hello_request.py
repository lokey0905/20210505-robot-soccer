from flask import Flask ,request
app = Flask(__name__)

@app.route('/')
def index():
    text = request.args.get('username')
    return 'Hello '+ text
    
if __name__ == '__main__':
    app.run(host='127.0.0.1')

