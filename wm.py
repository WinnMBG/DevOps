from flask import Flask, render_template
import pytest

app = Flask(__name__)

@app.route("/")
def hello_world():
   	return render_template('index.html')
   
@app.errorhandler(404)
def error_not_found(error):
   	return render_template('indexerror.html'), 404
   
@app.errorhandler(500)
def error_no_found(error):
	return render_template('indexerror.html'), 500
   
@app.route("/<name>/<number>")
def second(name, number):
    return render_template('index2.html', name=name, number=int(number))
   	    
if __name__== "__main__":
	app.run('0.0.0.0', port=5000)
