from flask import Flask, render_template

App = Flask(__name__)
PORT = 5000
DEBUG = True

@App.route('/')
def Principal():
    return render_template('index.html')

if __name__ == '__main__':
    App.run(port = PORT, debug=DEBUG)

