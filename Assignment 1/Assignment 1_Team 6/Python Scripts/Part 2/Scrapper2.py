from bs4 import BeautifulSoup
from urllib.request import urlopen




# Link for scrapping
url = "https://www.ffiec.gov/nicpubweb/content/BHCPRRPT/BHCPR_Peer.htm"
baseLink="https://www.ffiec.gov/nicpubweb/content/BHCPRRPT/"
html = urlopen(url)
finalList=[]
soup = BeautifulSoup(html, "html.parser")

#Code to filter in html elements
tbl = soup.findAll(class_='lightest')
for t in tbl:
    s=t.find_all('a')
    links=[link.attrs['href'] for link in s]
    for link in links:
     if "PeerGroup_1_" in link:
      finalList.append(link)

#Code to save PDF documents to the local system
for tempLink in finalList:
    navLink=baseLink+tempLink

    response = urlopen(navLink)
    tokens=tempLink.split('/')
    file = open(tokens[3], 'wb')
    file.write(response.read())

    file.close()

print("Completed")





