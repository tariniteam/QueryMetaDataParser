select a.col1 as 'Team_Col1', 
       a.col2 as 'Team_Col2',  
       a.col3 as 'Team_Col3', 
       l.col4 as 'Lead_Col4', 
       l.col5 as 'Lead_Col5', 
       l.col6 'Lead_col6', 
       l.col7 
from tblTeam a 
inner join tblLead l 
on a.col1 = l.col1 
where a.col1 = 'abc' 
and a.col3 = 'def' 
and l.col5 = 'abc'