# QueryMetaDataParser

## **Problem Statement**

The Query Metadata Parser solves many common and difficult SQL, including th following:
1.	Checks SQL syntax offline so that you can validate syntax without connecting to a database.
2.	It does an in-depth analysis of SQL Query passed as an input and comeup with SQL parse tree.
3.	It help in preventing SQL injection by giving information of how the predicates are used in the query.
4.	It help in identifying the how the table objects are used in the extraction of data from datawarehouse. 

## **Solution**

The Query metadata parser is used to deconstruct any sql query into individual components, where each components refers to some section of query construct. This help the analyst to get the catalog ready with the information of all the entity, attributes which are being used frequently by users.
The QMP has exposed its method and have UI where user can directly upload the query and get the parsed metadata delivered on the screen itself and also it has functionalty to download the desconstructed query. The various methods which are exposed for users are:
•	get_query_type 
◦	This method will give the information any the query type which could be DML or DDL or TCL statements
•	get_schema_list
◦	This will list out all the schemas where the objects are residing in database from the input query
•	get_table_list 
◦	This will list out all the tables involved in the sql query passed to the engine
•	get_column_list
◦	This will list out all the columns involved in the query along with its parent tables
•	get_filter_condition_list
◦	This will list out all the predicates used in the query.
•	get_joins_used 
◦	This will list of “kind of joins” used to join the various tables used in the sql query passed by user to system
•	get_all_metadata
◦	This will list out all the metadata which include tables, columns, predeicates, joins, schemas etc.


## **Architecture Diagram**

![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/QMP%20Architecture%20Diagram%20Final.png)

## **Parser**
The parser deconstructs the SQL query based on the SQL syntax, identifies each of the query components, and then creates an Abstract Syntax Tree in a hierarchical format. 

Add Diagram here 

## **Lexical Analysis/Tokenization**

The query parser break the the entire sql statment to various tokens, each token refer to one or other part of query. It forms a list of tokens, which will there after used to do the lexical analysis.

Add Diagram here 

## **Usage of Query Metadata Parser**

Help in identifying the mostly used tables in the data warehouse.
Help in knowing how each table are being queried and what kind of predicates are used in general to extract the data
Help in knowing how various tables are joined with each other.
Help in identifying various query pattern.

Having all above metrics available below question can be answered:
Popular tales and the attributes used in reporting.
Data set schemas metadata for perf optimization.
Joins information which will help in extablish the need for indexing and query tunning 



## **Prerequisites**

### Tools/Technologies used
1.	Python
2.	SQLite Database
3.	Jinja Framework
4.	Bootstrap Framework
5.	HTML, CSS

### Required Python packages
1.	Flask
2.	Sqlite3
3.	Sqlparse 

### Project Structure

---------QueryMetadataParser
         ├── __init__.py           # setup your app
         ├── query_parser.py       # Code for SQL Query Parsing
         ├── create_sqlite_db.py   # Database Creation 
         ├── app.py                # Flask Code
         ├── db.sqlite             # your database
         └── templates
             ├── display_all_metadata.html   # display all type of metadata
             ├── display_metadata.html       # display selected metadata
             ├── index.html                  # show the login form
             ├── successful_file_upload.html  # SQL script upload to directory 
             └── successful_login.html        # page after login
             └── type_of_metadata.html        # select type of metatdata
             └── upload_sql_script.html         # form to upload sql script
             └── style.css                      # css
         └── UploadedSQLScripts
             └── SQL_Script_1.html   # sql scripts uploaded in this directory
             └── SQL_Script_2.html   # sql scripts uploaded in this directory
          




## **Technical Implementation**

### I.	Prepare your Environment

1.	Create a virtual environment in python 

              virtualenv venv sql_parser

2.	Install the python packages in the virtual environment described in the pre-requisite section.

              flask
              sql-parser
              sqlite3

To install packages pip install package_name or you can create a new file requirements.txt (this file will contains one package name each row) and install all packages once using : pip install -r requirements.txt
 
3.	Create project structure as mentioned in the pre-requisite section.


### II.	Create Database

1.	Create Sqlite Database – QMP_DB.db

![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/1.%20QMP_DB.jpg)
 
2.	Create Tables dropdownlist and users in the database QMP_DB.db
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/2.%20DropdownList%20Table.jpg)
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/3.%20user%20table.jpg)


### III.	Create Web Pages

•	Enter user details and login to the Query Metadata Parser portal.

•	The application will validate the user details with the credentials stored in the Sqlite database and if it matches it will redirect to the next page. 
 
 ![alt text]( https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/4.%20login%20page.jpg)

•	Click on Analyze Metadata button post successful login.
 
 ![alt text]( https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/5.%20%20analyse%20metadata.jpg)
 
•	Choose a SQL Script from your local device and upload it to the portal.

![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/6.%20upload%20sql%20script.jpg )

![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/7.%20type%20of%20metadata.jpg )
 
 
•	Choose the type of Metadata that you want to display.
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/8..jpg)
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/9..jpg)
 
 
•	Based on the Metadata type selection, Metadata information would be displayed.
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/10..jpg )
 
•	Check other types of metadata by clicking on the button “Check other types of Metadata”.

![alt text]( https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/11..jpg)


### IV.	Connect Web Pages using the Flask Framework

•	Connect to sqlite database.

•	Create routing methods to route/redirect web pages based on the GET/POST.

## **Conclusion**



## **GitHub link**

•	https://github.com/tariniteam/QueryMetaDataParser  

## **Contributors**

1.	Harsha Navalkar ( https://www.linkedin.com/in/harsha-navalkar-00085515b/ )
2.	Vikram Mahapatra (https://www.linkedin.com/in/vikrammahapatra  )

