import sqlparse
from sqlparse import lexer
from sqlparse import sql, tokens as T
from sqlparse.compat import StringIO
from sqlparse.tokens import Name
from sqlparse.sql import IdentifierList, Identifier, Function


def token_to_list(token):
    token_list = list(token)
    return token_list

def get_query_type(first_non_whitespace_tokenize_tuple):
    query_type_lst = []
    # print(first_non_whitespace_tokenize_tuple)
    token_first_tuple_list = str(first_non_whitespace_tokenize_tuple[0]).split('.')
    query_category = token_first_tuple_list[::-1][0]
    query_type = first_non_whitespace_tokenize_tuple[1]    
    # result = {'Query Category': query_category, 'Query Type' : query_type}
    query_type_lst.append('Query Category --> ' + query_category )
    query_type_lst.append('Query Type --> ' + query_type )    
    return query_type_lst

def get_non_whitespace_token_list(token_list):
    """
    List consisting of Tokens without any space
    """
    token_list_without_wildspace = [item for item in token_list if str(item[0]) != 'Token.Text.Whitespace' and str(item[0]) != 'Token.Punctuation']
    # print(f'\nToken List without Whitespace:\nclscls {token_list_without_wildspace}')
    return token_list_without_wildspace


def parse_sql_query(tokens):  
    token_list = token_to_list(tokens)
    token_list_without_wildspace = get_non_whitespace_token_list(token_list)
    # print(token_list)
    
    #Query Type
    query_type = get_query_type(token_list[0])
    print(f'\nQueryTye:\n {query_type}')

    #Column List
    col_lst = get_column_list(token_list)
    print(f'Col List: \n {col_lst}')

    #Table List, schema name list, table alias lst
    table_name_lst, schema_name_lst, table_alias_lst = get_table_list(token_list)
   


def get_token_index(token_list,start,stop):
    """
        This method is used to get the index of Start and Stop literal index nunmber to calling method 
        return: start_index, stop_index
    """    
    start_index = 0
    stop_index = 0

    for index in range(len(token_list)):
        current_value = token_list[index]
        if (str(current_value[0]) == 'Token.Keyword' and str(current_value[1]) == start):
            start_index = index
        if (str(current_value[0]) == 'Token.Keyword' and str(current_value[1]) == stop):
            stop_index = index
    
    return start_index, stop_index

def get_table_list(token_list):
    start = 'from'
    stop = 'where'
    start_index, stop_index = get_token_index(token_list,start,stop)

    # print(start_index)
    # print(stop_index)

    from_token_list = []
    for index in range(len(token_list)):
        if index >= start_index and index <= stop_index:
            from_token_list.append(token_list[index])

    # print(from_token_list)
    token_list_without_wildspace = [item for item in from_token_list if str(item[0]) != 'Token.Text.Whitespace'] 
    # print(token_list_without_wildspace)
    
    table_name_lst = []
    schema_name_lst = []
    table_alias_lst = []
    join_lst = []
    join_lst_with_tbl = []

    for index in range(len(token_list_without_wildspace)):
        if(index + 3) <= len(token_list_without_wildspace) -1:
            current = token_list_without_wildspace[index]
            next = token_list_without_wildspace[index + 1]
            next_to_next = token_list_without_wildspace[index + 2]
            next_to_2_next = token_list_without_wildspace[index + 3]
            
            if(str(current[0]) == 'Token.Name' and str(next[0]) == 'Token.Punctuation' and str(next[1]) == '.' and str(next_to_next[0]) == 'Token.Name' and str(next_to_2_next[0]) == 'Token.Name'):
                schema = str(current[1])
                table = str(next_to_next[1])
                table_alias = str(next_to_2_next[1])
                # print(f"schema:{schema} table: {table} table_alias : {table_alias}")
                table_name_lst.append(str(schema) + '.' + str(table))
                schema_name_lst.append(str(schema))
                table_alias_lst.append(str(table_alias) + '-->' + str(table))

            if(str(current[0]) == 'Token.Keyword' and str(current[1]) in ['inner join', 'left join', 'right join']):
                join_lst.append(current[1])

    
    for index, join in enumerate(join_lst):
        join_lst_with_tbl.append(str(table_name_lst[index]) + '--> ' + str(join) + '--> ' + str(table_name_lst[index + 1]))

    print(f"Table List: {table_name_lst} \nSchema List: {schema_name_lst} \nTable Alias List: {table_alias_lst} \nJoin List : {join_lst_with_tbl}")
    return table_name_lst, schema_name_lst, table_alias_lst

def get_column_list(token_list):
    """
        This method is used to get the columns list 
    """
    col_lst = []
    print("\n")    
    for index in range(len(token_list)):   
        current_value = token_list[index]
        
        # print(f"Current Value: {current_value}")
        if not (index + 1 > len(token_list) - 1):
            next_value = token_list[index + 1]
            # print(f"Next Value: {next_value}")
        if not (index - 1 < 0):            
            prev_value = token_list[index - 1]
            # print(f"Prev Value: {prev_value}")        
        if  not (index + 2 > len(token_list) - 1):
            next_to_next_value = token_list[index + 2]
            # print(f"Next to Next Value: {next_value}")
     
        if (str(current_value[0]) == 'Token.Name' and str(next_value[1]) == '.' and str(next_to_next_value[0]) == 'Token.Name'):
            col = str(current_value[1]) + str(next_value[1]) + str(next_to_next_value[1] )
            col_lst.append(col)
            # print(str(current_value[1]) + str(next_value[1]) + str(next_to_next_value[1] ))

    return col_lst

if __name__ == "__main__":
  
    sql = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5', l.col6 'Lead_col6', l.col7 from rec.tblTeam a inner join reporting.tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"
    stream = StringIO(sql)
    tokens = lexer.tokenize(stream)
    parse_sql_query(tokens)
   
    # print('\nIdentifier')
    # print(Identifier)
    # print('\nIndentifier List')
    # print(IdentifierList)

    # parsed = sqlparse.parse(sql)[0]

    # print('First')

    # print(parsed.token_first().value)
    
    
    # print('vkm')
    # print(parsed)
    
    # print(parsed.tokens)
    # for item in parsed.tokens:
    #     print(item)
        

    quit()


      
    # lst = sql_tokenize(sql)
    # print(lst)

    # get_column_name(sql)
    

    # insert_stmt = parsed[0].token_first().value.lower() == "insert"
    # stream = extract_from_part(parsed[0], stop_at_punctuation=insert_stmt)
    # print( list(extract_table_identifiers(stream)))

    # print("")


    

    # # Cases for Simple select
    # sql = "select col1, col2, col3 from tblTeam"
    # sql2 = "select col1, col2, col3 from tblTeam where col1 = 'abc' and col3 = 'def'"
    # sql3 = "select a.col1, a.col2, a.col3 from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"    
    # sql4 = "select a.col1 as 'Column1', a.col2 as 'Column2', a.col3 as 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"
    # sql5 = "select a.col1 as 'Column1', a.col2, a.col3 as 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"
    # sql6 = "select a.col1 'Column1', a.col2 'Column2', a.col3 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"
    # sql7 = "select a.col1 'Column1', a.col2 as 'Column2', a.col3 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"

    # # Cases for simple Joins
    # # Inner Join
    # sql3 = "select a.col1, a.col2, a.col3 from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  

    # # Inner join but with only keyword JOIN
    # sql3 = "select a.col1, a.col2, a.col3 from tblTeam a join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  

    # # Left Join 
    # sql3 = "select a.col1, a.col2, a.col3 from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  

    # # Right Join 
    # sql3 = "select a.col1, a.col2, a.col3 from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  

    # # Full Outer Join 
    # sql3 = "select a.col1, a.col2, a.col3 from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    # sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    # sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  


