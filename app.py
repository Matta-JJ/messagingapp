'''app.py: This is my main application file where I define my Flask app and routes.'''


from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
