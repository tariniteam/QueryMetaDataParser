from flask import Flask, request, render_template, redirect,url_for, flash
import sqlite3 as sq
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './UploadedSQLScripts'
ALLOWED_EXTENSIONS = {'sql'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_query_type ():
    Jinja_list_QueryType = ['QueryType1', 'QueryType2']
    return Jinja_list_QueryType
def get_schema_list ():
    Jinja_list_Schemas = ['Schema1', 'Schema2']
    return Jinja_list_Schemas

def get_table_list ():
    Jinja_list_Tables = ['Table1', 'Table2']
    return Jinja_list_Tables

def get_column_list ():
    Jinja_list_Columns = ['Column1', 'Column2']
    return Jinja_list_Columns

def get_filter_condition_list ():
    Jinja_list_FilterConditions = ['Filter1', 'Filter2']
    return Jinja_list_FilterConditions

def get_joins_used ():
    Jinja_list_JoinsUsed = ['Join1', 'Join2']
    return Jinja_list_JoinsUsed

def get_all_metadata ():
    Jinja_list_AllMetadata = ['Metadata1', 'Metadata2']
    return Jinja_list_AllMetadata

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

@app.route('/successful_file_upload', methods=['GET', 'POST' ])
def type_of_metadata():
    #if request.method == 'POST':
        connection = sq.connect('QMP_DB.db')
        cursor = connection.cursor()
        #name_var = request.form['name_id']
        #password_var = request.form['password_id']
        dropdownlist ="SELECT name from dropdownlist order by name "
        cursor.execute(dropdownlist)
        results = cursor.fetchall()
        print ("DB Results", results)
        string_list = [''.join(i) for i in results]
        print ("Converted to String", string_list)
        return render_template('type_of_metadata.html', results=string_list)


@app.route('/type_of_metadata', methods=['GET', 'POST'])
def display_metadata():
        user_dropdown_selection = request.form.get('dropdownlist_option')
        print("user_dropdown_selection", user_dropdown_selection)

        Jinja_list_AllMetadata = get_all_metadata()
        Jinja_list_Columns  = get_column_list()
        Jinja_list_FilterConditions  = get_filter_condition_list()
        Jinja_list_JoinsUsed   = get_joins_used()
        Jinja_list_QueryType   = get_query_type()
        Jinja_list_Schemas  = get_schema_list()
        Jinja_list_Tables = get_table_list()

        if  (user_dropdown_selection == 'AllMetadata' ):
           return render_template('display_metadata.html', Jinja_list=Jinja_list_AllMetadata)
        elif (user_dropdown_selection == 'Columns' ):
           return render_template('display_metadata.html', Jinja_list=Jinja_list_Columns)
        elif (user_dropdown_selection == 'FilterConditions'):
           return render_template('display_metadata.html', Jinja_list=Jinja_list_FilterConditions)
        elif (user_dropdown_selection == 'JoinsUsed'):
           return render_template('display_metadata.html', Jinja_list=Jinja_list_JoinsUsed)
        elif (user_dropdown_selection == 'QueryType'):
           return render_template('display_metadata.html', Jinja_list=Jinja_list_QueryType)
        elif (user_dropdown_selection == 'Schemas'):
            return render_template('display_metadata.html', Jinja_list=Jinja_list_Schemas)
        elif (user_dropdown_selection == 'Tables'):
            return render_template('display_metadata.html', Jinja_list=Jinja_list_Tables)
        return render_template('display_metadata.html')

@app.route('/display_metadata', methods=['GET', 'POST'])
def choose_other_metadata_type():
    if request.method == 'POST':
        return render_template('type_of_metadata.html')

if __name__ == "__main__":
     app.run(debug=True)