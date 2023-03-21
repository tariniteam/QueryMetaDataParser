import sqlparse
from sqlparse import lexer
from sqlparse import sql, tokens as T
from sqlparse.compat import StringIO
from sqlparse.tokens import Name


def sql_tokenize(string):
    """ Tokenizes a SQL statement into tokens.

    Inputs:
       string: string to tokenize.

    Outputs:
       a list of tokens.
    """
    tokens = []
    statements = sqlparse.parse(string)

    # SQLparse gives you a list of statements.
    for statement in statements:
        # Flatten the tokens in each statement and add to the tokens list.
        flat_tokens = sqlparse.sql.TokenList(statement.tokens).flatten()
        for token in flat_tokens:
            strip_token = str(token).strip()
            if len(strip_token) > 0:
                tokens.append(strip_token)

    newtokens = []
    keep = True
    for i, token in enumerate(tokens):
        if token == ".":
            newtoken = newtokens[-1] + "." + tokens[i + 1]
            newtokens = newtokens[:-1] + [newtoken]
            keep = False
        elif keep:
            newtokens.append(token)
        else:
            keep = True

    return newtokens 

def get_column_name(qry):
        for parsed in sqlparse.parse(qry):
            for token in parsed.flatten():
                if token.ttype in Name:
                    print(token.value)

if __name__ == "__main__":
    # sql = "select * from (select t. from tabl t"
    # sql = "select abc, acv from tGHT where abc = 'a'"
    # print(extract_tables(sql))
    # parsed = sqlparse.parse(sql)
    
    # if not parsed:
    #     print("Nonthing to parse")
    #     quit()

    # par = parsed[0].t
    # print(parsed[0].token_first().value.lower())
    sql = "SELECT a.col1, b.col2, a.col3 from myFaltuTeam f full outer join myfaltuboss b where f.id = b.id where a.faltu_team_lead = 'yanarp' and a.saas ='manoop'"
    stream = StringIO(sql)
    tokens = lexer.tokenize(stream)
    # print(list(tokens))
    token_list = list(tokens)
    for item in token_list:
        print(item)
    query = [item[1] for item in token_list]
    print('a')
    print(query)

    
    lst = sql_tokenize(sql)
    print(lst)

    get_column_name(sql)
    
    quit()

    insert_stmt = parsed[0].token_first().value.lower() == "insert"
    stream = extract_from_part(parsed[0], stop_at_punctuation=insert_stmt)
    print( list(extract_table_identifiers(stream)))

    print("")


    

    # Cases for Simple select
    sql = "select col1, col2, col3 from tblTeam"
    sql2 = "select col1, col2, col3 from tblTeam where col1 = 'abc' and col3 = 'def'"
    sql3 = "select a.col1, a.col2, a.col3 from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"    
    sql4 = "select a.col1 as 'Column1', a.col2 as 'Column2', a.col3 as 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"
    sql5 = "select a.col1 as 'Column1', a.col2, a.col3 as 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"
    sql6 = "select a.col1 'Column1', a.col2 'Column2', a.col3 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"
    sql7 = "select a.col1 'Column1', a.col2 as 'Column2', a.col3 'Column3'  from tblTeam a where a.col1 = 'abc' and a.col3 = 'def'"

    # Cases for simple Joins
    # Inner Join
    sql3 = "select a.col1, a.col2, a.col3 from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a inner join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  

    # Inner join but with only keyword JOIN
    sql3 = "select a.col1, a.col2, a.col3 from tblTeam a join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  

    # Left Join 
    sql3 = "select a.col1, a.col2, a.col3 from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a left join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  

    # Right Join 
    sql3 = "select a.col1, a.col2, a.col3 from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a right join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  

    # Full Outer Join 
    sql3 = "select a.col1, a.col2, a.col3 from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def'"  
    sql3 = "select a.col1, a.col2, a.col3, l.col4, l.col5 from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a full outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  
    sql3 = "select a.col1 as 'Team_Col1', a.col2 as 'Team_Col2', a.col3 as 'Team_Col3', l.col4 as 'Lead_Col4', l.col5 as 'Lead_Col5' from tblTeam a outer join tblLead l on a.col1 = l.col1 where a.col1 = 'abc' and a.col3 = 'def' and l.col5 = 'abc'"  


    