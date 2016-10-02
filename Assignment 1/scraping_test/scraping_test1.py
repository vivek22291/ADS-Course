
from bs4 import BeautifulSoup
from lxml import html
import requests
from urllib.request import urlopen
import pandas as pd


url = "https://www.ffiec.gov/nicpubweb/nicweb/HCSGreaterThan10B.aspx"
html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")

rank = []
institutionName = []
location = []
totalAssets = []

table = soup.find(class_= 'datagrid')

for row in table.find_all('tr')[1:]:
    col = row.find_all('td')
    print(col)


    '''
    column_1 = col[0].string.strip()
    rank.append(column_1)
    column_2 = col[1].string.strip()
    institutionName.append(column_2)
    column_3 = col[2].string.strip()
    location.append(column_3)
    column_4 = col[3].string.strip()
    totalAssets.append(column_4)

    columns = {'rank' : rank, "institutionName" : institutionName, "location" : location, "totalAssets" : totalAssets}

    df = pd.dataframe(columns)

print(df)
'''
'''
#------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# url that we are scraping
url = "https://www.ffiec.gov/nicpubweb/nicweb/HCSGreaterThan10B.aspx"

# this is the html from the given url
html = urlopen(url)

soup = BeautifulSoup (html, "html.parser" )
print(soup)
soup.findAll('tr', limit=2)
soup.findAll('tr', limit=2)[1]
soup.findAll('tr', limit=2)[1].findAll('th')
column_headers = [th.getText() for th in
                  soup.findAll('tr', limit=2)[1].findAll('th')]
print(column_headers)

'''