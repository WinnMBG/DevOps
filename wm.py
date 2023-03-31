from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#import mysql.connector
#from mysql.connector import Error

# Flask app configuration and connection to database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@0.0.0.0/studentdb'
db = SQLAlchemy(app)

#def connect():
#	connection = None
	
#	try:
#		connection = mysql.connector.connect(host='localhost', database='studentdb', user='root', password='123456')	
		
#		if connection.is_connected():
#			print('Connected to the database')
#	except Error as e:
#		print(e)
		
#	finally:
#		if connection is not None and connetion.is_connected():
#			connection.close()

#Creating a Model
class Student(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	firstname=db.Column(db.String(20), unique=False, nullable=False) 
	lastname=db.Column(db.String(20), unique=False, nullable=False)
	age=db.Column(db.Integer, nullable=False)
	gender=db.Column(db.String(10), unique=False, nullable=False)
	
	def __repr__(self):
		return f"Name : {self.firstname}, Age : {self.age}"
	
#All the application routes
@app.route("/")
def hello_world():
   	return render_template('index.html')
   	
@app.route("/getAll")
def get_all():
	students = Student.query.all()
	return render_template('indexdb.html', students=students)
   
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
	#connect()
