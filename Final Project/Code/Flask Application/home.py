from flask import Flask,render_template, request,redirect,url_for
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import json
app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index_final.html')



@app.route('/HomePage')
def HomePage():
    return render_template('ModelPage.html')

# real time text analysis
@app.route('/RealTime')
def RealTime():
    return render_template('RealTime.html')

# result of the the Real time analysis
@app.route('/ResultRealTime')
def ResultRealTime():
    return render_template('ResultRealTime.html')

# consuming the JSON response of real time text analysis
@app.route('/Analysis',methods=['POST'])
def analyse():
      ubusinessName=request.form['businessName']
      resultingHighLows = []
      ubusinessName=ubusinessName.lower()
      rawbusinessName = ubusinessName + " Boston"
      businessName = rawbusinessName.replace(" ", "-")

      y = 0

      while y <= 100:
          reviewList = []
          url = "https://www.yelp.com/biz/" + businessName + "?start=" + str(y)
          scrapePage = urlopen(url)
          soup = BeautifulSoup(scrapePage)
          para = soup.find_all('div', class_="review-content")

          for p in para:
              s = p.find('p').text.strip()
              print(s)
              reviewList.append(s)

          print(len(reviewList))
          for reviews in reviewList:
              data = {
                  "Inputs": {
                      "input1": {
                          "ColumnNames": [
                              "text"

                          ],
                          "Values": [
                              [
                                  reviews
                              ]
                          ]
                      }
                  },
                  "GlobalParameters": {
                  }
              }

              body = str.encode(json.dumps(data))

              url = 'https://ussouthcentral.services.azureml.net/workspaces/e2fc148f234147b6b2981de7ef5cd7f4/services/f05d0dc5290347f8a5483ece2dff8b28/execute?api-version=2.0&details=true'
              api_key = 'xY5goIAlA58FHn31t2NysCxeqEyYo+C3P10pvAlSkpCxgtJur1CzfjhQDFtGsxRNqhAkRhHqptgVADW9gbcw9Q=='  # Replace this with the API key for the web service
              headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
              req = urllib.request.Request(url, body, headers)
              response = urllib.request.urlopen(req)
              result = response.read().decode("utf-8")
              jResult = json.loads(result)
              resultingHighLows.append(jResult['Results']['output1']['value']['Values'][0][0])
          y = y + 20
      commanElement=max(set( resultingHighLows), key= resultingHighLows.count)
      accuracy=int((resultingHighLows.count(commanElement)/len(resultingHighLows))*100)
      return render_template('ResultRealTime.html',values=resultingHighLows,business=ubusinessName.upper(),accuracy=accuracy,commanElement=commanElement)



if __name__ == '__main__':
   app.run(debug=True)