# QueryMetaDataParser

## **Problem Statement**

## **Solution**

## **Architecture Diagram**

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
2.	Vikram Mahapatra ()

