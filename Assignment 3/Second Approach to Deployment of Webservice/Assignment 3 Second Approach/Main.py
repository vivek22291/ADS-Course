from flask import Flask,render_template,request
import urllib.request
import json
import datetime

app=Flask(__name__,template_folder='template')


@app.route('/')
def index():
    return render_template('Main.html')

@app.route('/submit', methods=['POST'])
def process_data():
    date=request.form['date']
    time=request.form['hour']
    temperature=request.form['temperature']
    modelType=request.form['Model Type']
    newDate=datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%m/%d/%Y')

    if (modelType=='regression'):
     results=NeuralNetRegression(newDate,time,temperature);
     results2=RandomForestRegression(newDate,time,temperature);

     results4=LinearRegression(newDate,time,temperature);
    elif (modelType=='classification'):
     result5=NeuralNetClassification(newDate,time,temperature);
     result6 = RandomForestClassification(newDate,time,temperature);
     results3 = LogisticRegression(newDate, time, temperature);


     results="pool"

    if (modelType=='regression'):
     return results+"<br/>"+results2+"<br/>"+results4
    if (modelType=='classification'):
     return result5+"<br/>"+result6+"<br/>"+results3


def NeuralNetRegression(date,time,temperature ):
    data = {
        "Inputs":{
    "input1": {
      "ColumnNames": [
        "newDate",
        "hour",
        "TemperatureF"
      ],
      "Values": [
        [
          str(date),
          time,
          temperature
        ]
      ]
    }
  },
        "GlobalParameters": {
        }
    }
    #data={}
    #data['Time']=str(time)
    #data['Monetary']=str(date)
    #data['Class']=str(temperature)
    #data['Recency']="1"
    #data['Frequency']="1"


    body = str.encode(json.dumps(data))

    url = '	https://ussouthcentral.services.azureml.net/workspaces/0707deb3bd1349da9ab00020439a843e/services/4a34a264f2ac4ef690778bf84799e904/execute?api-version=2.0&details=true'
    api_key = 'wEtq99rBIH5TL8+YN9+tPQvE010xE/5bgkVtRzrrO4WqP6i3mhwQgYRKPbMVyDHiGFs4lg7Ak8eD3HypMt7S6w=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)


      #  response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)

    result = response.read()
    finalValues="Neural Network Regression:"+str(result)
    return finalValues



def RandomForestRegression(date,time,temperature ):
    data = {
        "Inputs":{
    "input1": {
      "ColumnNames": [
        "newDate",
        "hour",
        "TemperatureF"
      ],
      "Values": [
        [
          str(date),
          time,
          temperature
        ]
      ]
    }
  },
        "GlobalParameters": {
        }
    }
    #data={}
    #data['Time']=str(time)
    #data['Monetary']=str(date)
    #data['Class']=str(temperature)
    #data['Recency']="1"
    #data['Frequency']="1"


    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0707deb3bd1349da9ab00020439a843e/services/9a972c59959e42688b501f89165ccf18/execute?api-version=2.0&details=true'
    api_key = 'XgW4M0lNpJK2UEn6uh0ZKeju10j9GvkH+WzSjEoGUVMnewiGZkKmGSo68Jl2P2Mmu6p4Ubd8pAjIUhg26o9ZnQ=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)


      #  response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)

    result = response.read()
    finalValues="Random Forest Regression:"+str(result)
    return finalValues


def LogisticRegression(date,time,temperature ):
    data = {
        "Inputs":{
    "input1": {
      "ColumnNames": [
        "newDate",
        "hour",
        "TemperatureF"
      ],
      "Values": [
        [
          str(date),
          time,
          temperature
        ]
      ]
    }
  },
        "GlobalParameters": {
        }
    }
    #data={}
    #data['Time']=str(time)
    #data['Monetary']=str(date)
    #data['Class']=str(temperature)
    #data['Recency']="1"
    #data['Frequency']="1"


    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0707deb3bd1349da9ab00020439a843e/services/01de667d2a0d45faa86c6ec5c1a9a153/execute?api-version=2.0&details=true'
    api_key = 'v5tnbkdvU87YnSIc1TGRQD6OOKEB77o8kYg3zI6wmGhRrwPz7zXBcGUVoWDana0Fv0shQFBD3j4cv9rJlq/QJw=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)


      #  response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)

    result = response.read()
    finalValues="Logistic Regression:"+str(result)
    return finalValues



def LinearRegression(date,time,temperature ):
    data = {
        "Inputs":{
    "input1": {
      "ColumnNames": [
        "newDate",
        "hour",
        "TemperatureF"
      ],
      "Values": [
        [
          str(date),
          time,
          temperature
        ]
      ]
    }
  },
        "GlobalParameters": {
        }
    }
    #data={}
    #data['Time']=str(time)
    #data['Monetary']=str(date)
    #data['Class']=str(temperature)
    #data['Recency']="1"
    #data['Frequency']="1"


    body = str.encode(json.dumps(data))

    url = '	https://ussouthcentral.services.azureml.net/workspaces/0707deb3bd1349da9ab00020439a843e/services/196db16ec26c4b79a08224266fd80ff8/execute?api-version=2.0&details=true'
    api_key = 'wXCTm/rUm644GBEy56Pd0x7ox1l3S2Jz5W2+7aHQ1n0UieOXdhv2Bnp3CAht3ZW1917kyGCIpcVnRAsX/7rXKg=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)


      #  response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)

    result = response.read()
    finalValues="Linear Regression:"+str(result)
    return finalValues


def NeuralNetClassification(date,time,temperature ):
    data = {
        "Inputs":{
    "input1": {
      "ColumnNames": [
        "newDate",
        "hour",
        "TemperatureF"
      ],
      "Values": [
        [
          str(date),
          time,
          temperature
        ]
      ]
    }
  },
        "GlobalParameters": {
        }
    }
    #data={}
    #data['Time']=str(time)
    #data['Monetary']=str(date)
    #data['Class']=str(temperature)
    #data['Recency']="1"
    #data['Frequency']="1"


    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0707deb3bd1349da9ab00020439a843e/services/71b7a7bfe487474baff9c404d81f26c4/execute?api-version=2.0&details=true'
    api_key = 'PhhpLDDcO6+b5IX4V+Ae96uTpool6gvlarzitS2rYxV/5SZ/6ArhFSz/rAxMU4wNf6vzkDxwX9QEA7eUKRkZhQ=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)


      #  response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)

    result = response.read()
    finalValues="Neural Network Classification:"+str(result)
    return finalValues



def RandomForestClassification(date,time,temperature ):
    data = {
        "Inputs":{
    "input1": {
      "ColumnNames": [
        "newDate",
        "hour",
        "TemperatureF"
      ],
      "Values": [
        [
          str(date),
          time,
          temperature
        ]
      ]
    }
  },
        "GlobalParameters": {
        }
    }


    body = str.encode(json.dumps(data))

    url = '	https://ussouthcentral.services.azureml.net/workspaces/0707deb3bd1349da9ab00020439a843e/services/f93340ae871f4fd2bc861c1247086da2/execute?api-version=2.0&details=true'
    api_key = 'Vk5IyFRHoSQJOReQFcgfRyNm2EHRBBmtMEbXhaRAoYGcvKM6YoAsQXF77H6mPOl2U8SepIDINIL8CD5wkbfbXw=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)


      #  response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)

    result = response.read()
    finalValues="Random Forest Classification:"+str(result)
    return finalValues

if __name__ == '__main__':
    app.run(debug=True)