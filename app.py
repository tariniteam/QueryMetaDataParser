from flask import Flask, request, render_template, redirect,url_for, flash
import sqlite3 as sq
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './UploadedSQLScripts'
ALLOWED_EXTENSIONS = {'sql'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        #f = request.files['file']
        #f.save(f.filename)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("successful_file_upload.html", name=filename)

@app.route('/successful_file_upload', methods = ['POST'])
def display_metadata():
    if request.method == 'POST':
        return render_template('display_metadata.html')

if __name__ == "__main__":
     app.run(debug=True)