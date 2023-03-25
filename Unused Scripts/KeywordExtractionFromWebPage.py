import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

class KeywordExtractionFromWebPage():

    def __init__(self, url):
        self.url = url

    def get_sql_keyword_list(self):
        html_response = requests.get(url=self.url)
        html_data = html_response.text
        soup = BeautifulSoup(html_data, 'html.parser')
        print('Extracted Table Extract DataFrame')
        table = soup.find_all('table')
        df = pd.read_html(str(table))[0]
        keyword_list = df.iloc[:,0].tolist()
        return keyword_list

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_SQL_reserved_words'
    objKeyWordExtraction = KeywordExtractionFromWebPage(url)
    keyword_list = objKeyWordExtraction.get_sql_keyword_list()
    print (keyword_list)
