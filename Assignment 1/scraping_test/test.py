# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://www.koreabaseball.com/Record/Player/HitterDetail/Game.aspx?playerId=76325'
#
# with requests.Session() as session:
#     session.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                                      ' Chrome/53.0.2785.116 Safari/537.36'}
#
#     # parsing parameters
#     response = session.get(url)
#     soup = BeautifulSoup([response.content], "html.parser")
#
#     data = {
#         'ctl00$ctl00$cphContainer$cphContents$ddlYear': '2013',
#         'ctl00$ctl00$txtSearchWord': '',
#         '__EVENTTARGET': soup.find('input', {'name': '__EVENTTARGET'}).get('value', ''),
#         '__EVENTARGUMENT': soup.find('input', {'name': '__EVENTARGUMENT'}).get('value', ''),
#         '__LASTFOCUS': soup.find('input', {'name': '__LASTFOCUS'}).get('value', ''),
#         '__VIEWSTATE': soup.find('input', {'name': '__VIEWSTATE'}).get('value', ''),
#         '__VIEWSTATEGENERATOR': soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value', ''),
#         '__EVENTVALIDATION': soup.find('input', {'name': '__EVENTVALIDATION'}).get('value', ''),
#     }
#
#     # parsing data
#     response = session.post(url, data=data)
#
#     soup = BeautifulSoup(response.content)
#
#     for row in soup.select('table.tData01 tr'):
#         print(td.text for td in row.find_all('td'))


from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import csv

apmc = '20160630'

url = 'https://www.ffiec.gov/nicpubweb/nicweb/HCSGreaterThan10B.aspx'
with requests.Session() as session:
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/53.0.2785.116 Safari/537.36'
    }
    response = session.get(url)
    soup = BeautifulSoup(urlopen(url), 'html.parser')

    # build an options mapping
    options = {option.get_text(strip=True): option['value'] for option in soup.select("select#cpMainContent_cmb_comm option")[1:]}

    # parse form parameters to get the form with the table
    form = soup.find("form", id="Form1")

    params = {
        'DateDropDown': options.get(apmc),
        '__ASYNCPOST': 'true',
        'ctl00$cpMainContent$ScriptManager1': 'ctl00$cpMainContent$UpdatePanel1|ctl00$cpMainContent$cmb_comm',
        '__EVENTTARGET': 'ctl00$cpMainContent$cmb_comm',
        '__EVENTARGUMENT': form.find('input', {'name': '__EVENTARGUMENT'})['value'],
        '__LASTFOCUS': '',
        '__VIEWSTATE': form.find('input', {'name': '__VIEWSTATE'})['value'],
        '__VIEWSTATEGENERATOR': form.find('input', {'name': '__VIEWSTATEGENERATOR'})['value'],
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': form.find('input', {'name': '__EVENTVALIDATION'})['value']
    }

    response = session.post(url, data=params)
    '''
    # parse the results
    soup = BeautifulSoup(response.content)
    for row in soup.select("table#cpMainContent_GridView1_tab5 tr")[1:]:
        print(row.find_all("td")[2].text)


    for row in soup.select('table.tData01 tr'):
        print([td.text for td in row.find_all('td')])
    '''


    #soup = BeautifulSoup(url, "html.parser")
    # list to store the rank, institution name, location, total_assets
    rank = []
    institution_name = []
    location = []
    total_assets = []
    quarter_date = []
    final_list = []

    tbl = soup.find(class_='datagrid')
    print(tbl)

    # get the row information
    rows = tbl.findAll('tr')
    count = 1
    with open('test1.csv', 'w') as output:
        fieldnames = ['rank', 'institution_name', 'location', 'total_assets']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        for row in rows:
            # to get the data for all the rows in the table
            while count < len(rows):
                # get the td information
                cols = rows[count].find_all('td')
                # get the a href info
                name = cols[1].find_all('a')
                # extract the rank and append to the list
                rank = cols[0].string
                # extract the name of the bank and append to the list
                institution_name = name[0].string
                # extract the location of the bank and append to the list
                location = cols[2].string

                # extract the bank assets and append to the list
                total_assets = cols[3].string
                final_list.append(cols[0].string)
                final_list.append(name[0].string)
                final_list.append(cols[2].string)
                final_list.append(cols[3].string)

                writer.writerow({'rank': rank, 'institution_name': institution_name, 'location': location,
                                 'total_assets': total_assets})
                count += 1