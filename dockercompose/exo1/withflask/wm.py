from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<a href='http://localhost:8080/'>Hello, World!</p>"

if __name__== "__main__":
   app.run('0.0.0.0', port=5000)
