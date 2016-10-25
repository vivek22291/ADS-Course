from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv
import pandas as pd
import numpy as np

# link to the website
url = 'https://www.ffiec.gov/nicpubweb/nicweb/HCSGreaterThan10B.aspx'
# to store the dates so that we can associate the banks with the assets to the years
dates = []

# get the web parameters
html = urlopen(url)

with requests.Session() as session:
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
                      }

    # parsing parameters
    # make a get request
    response = session.get(url)
    # returns HTML Document
    soup = BeautifulSoup(response.content, "html.parser")
    for option in soup.find_all('option'):
        dates.append(option.text)

    bit = 1
    for date in dates:
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # returns HTML Document

        data = {
            'DateDropDown': date,

            '__EVENTTARGET': soup.find('input', {'name': '__EVENTTARGET'}).get('value', ''),
            '__EVENTARGUMENT': soup.find('input', {'name': '__EVENTARGUMENT'}).get('value', ''),
            '__LASTFOCUS': soup.find('input', {'name': '__LASTFOCUS'}).get('value', ''),
            '__VIEWSTATE': soup.find('input', {'name': '__VIEWSTATE'}).get('value', ''),
            '__VIEWSTATEGENERATOR': soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value', ''),
            '__EVENTVALIDATION': soup.find('input', {'name': '__EVENTVALIDATION'}).get('value', ''),
        }

        # parsing data
        response = session.post(url, data=data)
        soup = BeautifulSoup(response.content)
        tbl = soup.find(class_='datagrid')

        if tbl is None:
            soup = BeautifulSoup(html, "html.parser")

            tbl = soup.find(class_='datagrid')
        rows = tbl.findAll('tr')
        count = 1

        with open('Test21.csv', 'a') as output:
            fieldnames = ['rank', 'institution_name', 'location', 'total_assets', 'quarter']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            for row in rows:
                # to get the data for all the rows in the table
                while count < len(rows):
                    # get the td information
                    cols = rows[count].find_all('td')
                    # get the a href info
                    name = cols[1].find_all('a')
                    institution_name = name[0].string
                    # extract the rank and append to the list
                    rank = cols[0].string
                    # extract the name of the bank and append to the list
                    # institution_name = name[0].string
                    # extract the location of the bank and append to the list
                    location = cols[2].string
                    # extract the bank assets and append to the list
                    total_assets = cols[3].string
                    quarter = date
                    writer.writerow({'rank': rank, 'institution_name': institution_name, 'location': location,
                                     'total_assets': total_assets, 'quarter': quarter})
                    count += 1

with open('Test21.csv') as input, open('Consolidated.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)


df = pd.read_csv('C:\\Users\\Vivek\\Desktop\\ADS\\Assignments\\ADS-Course\\Assignment 1\\scraping_test\\Consolidated.csv', names=['Rank', 'Institution Name', 'Location', 'Assets', 'Quarter'])

a = df[df['Quarter'] == 20160630]
print(a)
#pivot_nl = df.pivot(index=["Institution Name"], values=['Rank'], columns='Quarter')
#print(pivot_nl)
#pivot_according_to_name_location = pd.pivot_table(df,index=["Institution Name","Location"])
#print(pivot_according_to_name_location)

