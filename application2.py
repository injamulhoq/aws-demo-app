import mysql.connector
from flask import Flask,render_template,request

conn=mysql.connector.connect(host="database-2.caysf6rusuf9.us-east-2.rds.amazonaws.com",user="admin",password="bijli123",database="bookdb")
mycursor=conn.cursor()

application=Flask(__name__)

@application.route('/')
def index():
	mycursor.execute("SELECT * FROM books")
	data=mycursor.fetchall()
	return render_template('index.html', data=data)

@application.route('/add')
def add():

	return render_template('addbooks.html')

@application.route('/insert', methods=['POST'])
def insert():
	name=request.form.get('name')
	author=request.form.get('author')
	year=request.form.get('year')
	poster=request.form.get('poster')

	mycursor.execute("INSERT INTO books(id,name,author,year,poster) VALUES (NULL,'{}','{}','{}','{}')".format(name,author,year,poster))

	conn.commit()

	return render_template('addbooks.html')



if __name__=="__main__":
	application.run(debug=True)


	