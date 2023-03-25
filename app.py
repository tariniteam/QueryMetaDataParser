from flask import Flask, request, render_template, redirect,url_for
import sqlite3 as sq
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST' ])
def index():
 if request.method =='POST':
   connection = sq.connect('QMP_DB.db')
   cursor = connection.cursor()

   name_var=request.form['name_id']
   password_var= request.form['password_id']
   #print (name, password)

   query= "SELECT name, password from users where name='"+name_var+"' and password= '"+password_var+"'"
   cursor.execute(query)
   results = cursor.fetchall()

   if len(results) ==0:
       return ("Sorry Incorrect Credentials provided! Try again")
   else:
       return render_template("successful_login.html")
 return render_template('index.html')

@app.route('/successful_login', methods=['GET', 'POST' ])
def successful_login():
  if request.method =='POST':
    return render_template('upload_sql_script.html')

@app.route('/upload_sql_script', methods=['GET', 'POST' ])
def upload_sql_script():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("successful_file_upload.html", name = f.filename)

@app.route('/successful_file_upload', methods = ['POST'])
def display_metadata():
    if request.method == 'POST':
        return render_template('display_metadata.html')

if __name__ == "__main__":
     app.run(debug=True)