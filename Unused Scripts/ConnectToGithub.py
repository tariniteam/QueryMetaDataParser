import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

class ConnectToGithub():

    def __init__(self, base_github_folder):
        self.base_github_folder = base_github_folder
        self.list_of_files = []
        self.sql_scripts_df = pd.DataFrame()

        self.base_dir = base_github_folder
        self.base_dir = self.base_dir.replace('https://github.com', '')
        self.base_dir = self.base_dir.rsplit('/', 1)[-1] + '/'
        print("base_dir", self.base_dir)

        for link in self.get_list_of_files(self.base_github_folder):
            if self.base_dir in link and '.sql' in link:
                link = 'https://github.com' + link
                self.list_of_files.append(link)
                self.sql_scripts_df = self.sql_scripts_df.append(self.read_sql_scripts(link))

        df = self.return_sql_script_data_frame()
        print("List of SQL Script Files", self.list_of_files)
        print("SQL Scripts DataFrame ", self.sql_scripts_df)

    def get_list_of_files(self, url):
        soup = BeautifulSoup(requests.get(url).text)
        for a in soup.find_all('a'):
            yield a['href']

    def return_sql_script_data_frame(self):
        df = self.sql_scripts_df
        return df

    def read_sql_scripts(self, url):
        html_response = requests.get(url=url)
        html_data = html_response.text
        soup = BeautifulSoup(html_data, 'html.parser')
        print('SQL Scripts')
        table = soup.find_all('table')
        df = pd.read_html(str(table))[0]
        print("Dataframe", df)
        sql_scripts = df.iloc[:, 1].tolist()
        print ("SQL Scripts",sql_scripts )
        return sql_scripts

if __name__ == "__main__":
    base_github_folder = 'https://github.com/tariniteam/hack_the_hackathon/tree/main/Query%20Metadata%20Parser/SQL%20Scripts'
    objConnectToGithub = ConnectToGithub(base_github_folder)
    #list_output = objConnectToGithub.get_list_of_files(base_github_folder)
    #print(list_output)




