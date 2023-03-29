from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
   return render_template('index.html')
   
@app.route("/<name>/<number>")
def second(name, number):
   return render_template('index2.html', name=name, number=int(number))

if __name__== "__main__":
   app.run('0.0.0.0', port=5000)
