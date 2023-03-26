from flask import Flask, request, render_template, redirect,url_for, flash
import sqlite3 as sq
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './UploadedSQLScripts'
ALLOWED_EXTENSIONS = {'sql'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_query_type ():
    Jinja_list_QueryType = ['DML --> Select']
    return Jinja_list_QueryType

def get_schema_list ():
    Jinja_list_Schemas = ['rec --> tblTeam', 'reporting --> tblLead']
    return Jinja_list_Schemas

def get_table_list ():
    Jinja_list_Tables = ['rec.tblTeam', 'reporting.tblLead']
    return Jinja_list_Tables

def get_column_list ():
    Jinja_list_Columns = ['rec.tblTeam.Col1', 'rec.tblTeam.Col2', 'reporting.tblLead.Col4','reporting.tblLead.Col5', 'reporting.tblLead.Col6', 'reporting.tblLead.Col7' ]
    return Jinja_list_Columns

def get_filter_condition_list ():
    Jinja_list_FilterConditions = ['a.col1 = ''abc'''', 'a.col3 = ''def'' ', 'l.col5 = ''abc''' ]
    return Jinja_list_FilterConditions

def get_joins_used ():
    Jinja_list_JoinsUsed = ['inner join (Ltbl) --> rec.tblTeam ', 'inner join (Rtbl) --> reporting.tblLead']
    return Jinja_list_JoinsUsed

def get_all_metadata ():
    Jinja_list_QueryType = ['QueryType1', 'QueryType2']
    Jinja_list_Schemas = ['Schema1', 'Schema2']
    Jinja_list_Tables = ['Table1', 'Table2']
    Jinja_list_Columns = ['Column1', 'Column2']
    Jinja_list_FilterConditions = ['Filter1', 'Filter2']
    Jinja_list_JoinsUsed = ['Join1', 'Join2']
    return Jinja_list_QueryType, Jinja_list_Schemas, Jinja_list_Tables, Jinja_list_Columns, Jinja_list_FilterConditions, Jinja_list_JoinsUsed

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

        if  (user_dropdown_selection == 'AllMetadata' ):
           Header_For_MetaData = "All Metadata:"
           Jinja_list_QueryType, Jinja_list_Schemas, Jinja_list_Tables, Jinja_list_Columns, Jinja_list_FilterConditions, Jinja_list_JoinsUsed = get_all_metadata()
           Jinja_list_AllMetadata = [{'header': 'Query Types:' , 'data': Jinja_list_QueryType},
                                     {'header': 'Schemas:'     , 'data': Jinja_list_Schemas},
                                     {'header': 'Tables:'      , 'data': Jinja_list_Tables},
                                     {'header': 'Columns:'     , 'data': Jinja_list_Columns},
                                     {'header':'Filters:'      , 'data': Jinja_list_FilterConditions},
                                     {'header': 'Joins:'       , 'data': Jinja_list_JoinsUsed} ]
           return render_template('display_all_metadata.html', Jinja_list_AllMetadata=Jinja_list_AllMetadata, Header_For_MetaData= Header_For_MetaData )

        elif (user_dropdown_selection == 'Columns' ):
           Header_For_MetaData = "Column Metadata:"
           Jinja_list_Columns = get_column_list()
           return render_template('display_metadata.html', Jinja_list=Jinja_list_Columns, Header_For_MetaData= Header_For_MetaData)
        elif (user_dropdown_selection == 'FilterConditions'):
           Header_For_MetaData = "Filter Conditions Metadata:"
           Jinja_list_FilterConditions = get_filter_condition_list()
           return render_template('display_metadata.html', Jinja_list=Jinja_list_FilterConditions, Header_For_MetaData= Header_For_MetaData)
        elif (user_dropdown_selection == 'JoinsUsed'):
           Header_For_MetaData = "Joins Used Metadata:"
           Jinja_list_JoinsUsed = get_joins_used()
           return render_template('display_metadata.html', Jinja_list=Jinja_list_JoinsUsed, Header_For_MetaData =Header_For_MetaData)
        elif (user_dropdown_selection == 'QueryType'):
           Header_For_MetaData = "Query type Metadata:"
           Jinja_list_QueryType = get_query_type()
           return render_template('display_metadata.html', Jinja_list=Jinja_list_QueryType, Header_For_MetaData =Header_For_MetaData)
        elif (user_dropdown_selection == 'Schemas'):
            Header_For_MetaData = "Schema Metadata:"
            Jinja_list_Schemas = get_schema_list()
            return render_template('display_metadata.html', Jinja_list=Jinja_list_Schemas, Header_For_MetaData=Header_For_MetaData)
        elif (user_dropdown_selection == 'Tables'):
            Header_For_MetaData = "Table Metadata:"
            Jinja_list_Tables = get_table_list()
            return render_template('display_metadata.html', Jinja_list=Jinja_list_Tables,Header_For_MetaData= Header_For_MetaData)
        return render_template('display_metadata.html')

@app.route('/display_metadata', methods=['GET', 'POST'])
def choose_other_metadata_type():
    if request.method == 'POST':
        return render_template('type_of_metadata.html')

if __name__ == "__main__":
     app.run(debug=True)