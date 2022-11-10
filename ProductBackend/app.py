from flask import Flask
import receiver

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello")
    return "<p>Hello, Worsld!</p>"

if __name__ == '__main__':
   app.run(debug=True)