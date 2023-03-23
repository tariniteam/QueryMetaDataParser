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
    # print(first_non_whitespace_tokenize_tuple)
    token_first_tuple_list = str(first_non_whitespace_tokenize_tuple[0]).split('.')
    query_category = token_first_tuple_list[::-1][0]
    query_type = first_non_whitespace_tokenize_tuple[1]    
    result = {'Query Category': query_category, 'Query Type' : query_type}
    return result

def get_non_whitespace_token_list(token_list):
    """
    List consisting of Tokens without any space
    """
    token_list_without_wildspace = [item for item in token_list if str(item[0]) != 'Token.Text.Whitespace' and str(item[0]) != 'Token.Punctuation']
    print(f'\nToken List without Whitespace:\nclscls {token_list_without_wildspace}')
    return token_list_without_wildspace
    
def extract_table_identifiers(token_stream):
    pass
    # """yields tuples of (schema_name, table_name, table_alias)"""

    # for item in token_stream:
    #     if isinstance(item, IdentifierList):
    #         for identifier in item.get_identifiers():
    #             # Sometimes Keywords (such as FROM ) are classified as
    #             # identifiers which don't have the get_real_name() method.
    #             try:
    #                 schema_name = identifier.get_parent_name()
    #                 real_name = identifier.get_real_name()
    #             except AttributeError:
    #                 continue
    #             if real_name:
    #                 yield (schema_name, real_name, identifier.get_alias())


def parse_sql_query(tokens):  
    token_list = token_to_list(tokens)
    query_type = get_query_type(token_list[0])
    print(f'\nQueryTye:\n {query_type}')

    token_list_without_wildspace = get_non_whitespace_token_list(token_list)
   
    for item in token_list_without_wildspace:
        print(item) 

    # query = [item[1] for item in token_list]    
    # print(query)

if __name__ == "__main__":
  
    sql = "select col1, col2, col3 from stg.tblTeam a inner join tblLead  b where col1 = 'abc'"
    stream = StringIO(sql)
    tokens = lexer.tokenize(stream)
    parse_sql_query(tokens)
   
    print('\nIdentifier')
    print(Identifier)
    print('\nIndentifier List')
    print(IdentifierList)

    parsed = sqlparse.parse(sql)[0]
    
    print(parsed)
    print(parsed.tokens)
    for item in parsed.tokens:
        print(item)

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


