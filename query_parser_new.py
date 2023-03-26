import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML


def is_subselect(parsed):
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        if from_seen:
            if is_subselect(item):
                for x in extract_from_part(item):
                    yield x
            elif item.ttype is Keyword:
                raise StopIteration
            else:
                yield item
        elif item.ttype is Keyword and item.value.upper() == 'FROM':
            from_seen = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        # print(item)
        # quit()
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                print(identifier.get_name())
                yield identifier.get_name()
        elif isinstance(item, Identifier):
            yield item.get_name()
        # It's a bug to check for Keyword here, but in the example
        # above some tables names are identified as keywords...
        elif item.ttype is Keyword:
            yield item.value


def extract_tables(sql):
    stream = extract_from_part(sqlparse.parse(sql)[0])
    print(stream)
    # quit()
    return list(extract_table_identifiers(stream))


if __name__ == '__main__':
    # sql = """
    # select K.a,K.b from (select H.b from (select G.c from (select F.d from
    # (select E.e from A, B, C, D, E), F), G), H), I, J, K order by 1,2;
    # """
    sql = "select col1, col2, col3 from stg.tblTeam a inner join tblLead b on  a.col1 = b.col3 where col3 = 'abc'"


    tables = ', '.join(extract_tables(sql))
    print('Tables: {0}'.format(tables))