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

1.	get_query_type

         This method will give the information any the query type which could be DML or DDL or TCL statements

2.	get_schema_list
	
         This will list out all the schemas where the objects are residing in database from the input query

3.	get_table_list 
	
         This will list out all the tables involved in the sql query passed to the engine

4.	get_column_list
	
         This will list out all the columns involved in the query along with its parent tables

5.	get_filter_condition_list
	
         This will list out all the predicates used in the query.

6.	get_joins_used
	
         This will list of “kind of joins” used to join the various tables used in the sql query passed by user to system

7.	get_all_metadata
	
         This will list out all the metadata which include tables, columns, predeicates, joins, schemas etc.


## **Architecture Diagram**


![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/QMP%20Architecture%20Diagram%20Final.png)


## **Parser**


The parser deconstructs the SQL query based on the SQL syntax, identifies each of the query components, and then creates an Abstract Syntax Tree in a hierarchical format. 


![alt text]( https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/Parser%20Diagram.png)


## **Lexical Analysis/Tokenization**

The query parser break the the entire sql statment to various tokens, each token refer to one or other part of query. It forms a list of tokens, which will there after used to do the lexical analysis.


![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/Lexical%20Analyser.png )


## **Usage of Query Metadata Parser**


1. Help in identifying the mostly used tables in the data warehouse.
2. Help in knowing how each table are being queried and what kind of predicates are used in general to extract the data
3. Help in knowing how various tables are joined with each other.
4. Help in identifying various query pattern.


Having all above metrics available below question can be answered:
1. Popular tales and the attributes used in reporting.
2. Data set schemas metadata for perf optimization.
3. Joins information which will help in extablish the need for indexing and query tunning 


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


![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/Project%20Structure.png)


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

The Query Metadata Parser help in deconstruct the SQL passed as an input to the lowest granulaity which will help analyst to take decision pertaining to DB tunning. The above parser can be extended futher to connected to the GIT repo and read all the sql and create Metadata catalog from it. It can also be extended to have metadata catalog versioned for any changes in the query.

## **GitHub link**

•	https://github.com/tariniteam/QueryMetaDataParser  

## **Contributors**

1.	Harsha Navalkar ( https://www.linkedin.com/in/harsha-navalkar-00085515b/ )
2.	Vikram Mahapatra (https://www.linkedin.com/in/vikrammahapatra  )

