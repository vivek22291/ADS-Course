
import numpy as np
import datetime
import pandas as pd

from pandas import DataFrame,read_csv
st=pd.DataFrame(read_csv("C:\\Users\\kalli\\OneDrive\\Documents\\Assignment 2(1)\\rawData1.csv",sep=','))
col_list=list(st)
st.reset_index(level=0, inplace=True)
i=0
y=5
z=16
print(list(st.columns.values))
while i<=23:
 st[i]=st[col_list[y:z]].sum(axis=1)
 y=z+1
 z=y+11
 i+=1
st.drop(st.columns[5:-24], axis=1,inplace=True)
temp=pd.DataFrame(st[:])
temp.drop(temp.columns[5:],axis=1,inplace=True)
df = st[(st.Units != 'kVARh')]
tf=df[(df.Units!='Power Factor')]
tf.drop(tf.columns[0:5],axis=1,inplace=True)
ls=pd.DataFrame(tf.stack())
ls.reset_index(level=1, inplace=True)
ls.columns=['hour','kwh']
print(len (ls.columns))
ls['index']=ls.index
result=temp.merge(ls,on='index',how='inner')
result['Date']=pd.to_datetime(result['Date'])
result['Month'],result['Day'],result['Year'],result['Day of Week']=result['Date'].dt.month,result['Date'].dt.day,result['Date'].dt.year,(result['Date'].dt.dayofweek+1)%7
#result['Weekday']=result['Date'].dt.dayofweek
peakIndicator = ((7<=result['hour']) & (result['hour']<=19))
result['peakHour']=np.where(peakIndicator,1,0)
result=result[result.Channel!='507115423 1 kWh']
result=result[result.Channel!='507115423 3']



times=['12:54 AM','1:54 AM','2:54 AM','3:54 AM','4:54 AM','5:54 AM','6:54 AM','7:54 AM','8:54 AM','9:54 AM','10:54 AM','11:54 AM','12:54 PM','1:54 AM','2:54 AM','3:54 AM','4:54 AM','5:54 AM','6:54 AM','7:54 AM','8:54 AM','9:54 AM','10:54 AM','11:54 AM']

for index,rows in result.iterrows():



 temp=datetime.datetime.strptime(str(rows['Date']),'%Y-%m-%d %H:%M:%S').date()
 newDate=temp.strftime("%Y%m%d")
 dates=newDate

 Month=str(rows['Month'])
 Day=str(rows['Day'])
 HideSpecis=1
 format=1
 url='https://www.wunderground.com/history/airport/KBOS/2014/'+Month+'/'+Day+'/DailyHistory.html'

 url2='https://www.wunderground.com/history/airport/KBOS/2014/'+Month+'/'+Day+'/DailyHistory.html?HideSpecis=1&format=1'
 data=pd.DataFrame(pd.read_csv(url2))
 if (temp.isoweekday() in range(1, 6)):
     result.set_value(index,'Weekday', '1')
 else:
     result.set_value(index,'Weekday', '0')

 header=data.columns.values
 DewPointF=''
 print(times[rows['hour']])
 print (dates)
 timeStandard=header[0]

 if times[rows['hour']] in list(data[timeStandard]):
    TemperatureF=data.loc[data[timeStandard]==times[rows['hour']],'TemperatureF']
    DewPointF=data.loc[data[timeStandard]==times[rows['hour']],'Dew PointF']
    Humidity= data.loc[data[timeStandard]==times[rows['hour']],'Humidity']
    SeaLevelPressure=data.loc[data[timeStandard]==times[rows['hour']],'Sea Level PressureIn']
    VisibilityMPH=data.loc[data[timeStandard]==times[rows['hour']],'VisibilityMPH']
    WindDirection=data.loc[data[timeStandard]==times[rows['hour']],'Wind Direction']
    WindSpeedMPH=data.loc[data[timeStandard]==times[rows['hour']],'Wind SpeedMPH']
    Conditions=data.loc[data[timeStandard]==times[rows['hour']],'Conditions']
    WindDirDegrees= data.loc[data[timeStandard]==times[rows['hour']],'WindDirDegrees']
    print (WindDirDegrees.iloc[0])
    result.set_value(index,'Temperature',str(TemperatureF.iloc[0]))
    result.set_value(index,'Dew_PointF',str(DewPointF.iloc[0]))
    result.set_value(index, 'Humidity',str(Humidity.iloc[0]))
    result.set_value(index, 'Sea_Level_PressureIn',str(SeaLevelPressure.iloc[0]))
    result.set_value(index, 'VisibilityMPH', str(VisibilityMPH.iloc[0]))
    result.set_value(index, 'WIND_Direction',str(WindDirection.iloc[0]) )
    result.set_value(index, 'Wind_SpeedMPH', str(WindSpeedMPH.iloc[0]))
    result.set_value(index, 'Conditions', str(Conditions.iloc[0]))
    result.set_value(index, 'WindDirDegress',str(WindDirDegrees.iloc[0]))


result=result[['Account','Date','kwh','Month','Day','Year','hour','Day of Week','Weekday','peakHour','Temperature','Dew_PointF','Humidity','Sea_Level_PressureIn','VisibilityMPH','WIND_Direction','Wind_SpeedMPH','Conditions','WindDirDegress']]



pd.DataFrame(result).to_csv("First6Months_10_26_2016.csv", sep=',')


#2nd Part


st=pd.DataFrame(read_csv("C:\\Users\\kalli\\OneDrive\\Documents\\Assignment 2(1)\\rawData2.csv",sep=','))
col_list=list(st)
st.reset_index(level=0, inplace=True)
i=0
y=5
z=16

while i<=23:
 st[i]=st[col_list[y:z]].sum(axis=1)
 y=z+1
 z=y+11
 i+=1
st.drop(st.columns[5:-24], axis=1,inplace=True)
temp=pd.DataFrame(st[:])
temp.drop(temp.columns[5:],axis=1,inplace=True)
df = st[(st.Units != 'kVARh')]
tf=df[(df.Units!='Power Factor')]
tf.drop(tf.columns[0:5],axis=1,inplace=True)
ls=pd.DataFrame(tf.stack())
ls.reset_index(level=1, inplace=True)
ls.columns=['hour','kwh']

ls['index']=ls.index
result2=temp.merge(ls,on='index',how='inner')
result2['Date']=pd.to_datetime(result2['Date'])
result2['Month'],result2['Day'],result2['Year'],result2['Day of Week']=result2['Date'].dt.month,result2['Date'].dt.day,result2['Date'].dt.year,(result2['Date'].dt.dayofweek+1)%7
#result2['Weekday']=result2['Date'].dt.dayofweek
peakIndicator = ((7<=result2['hour']) & (result2['hour']<=19))
result2['peakHour']=np.where(peakIndicator,1,0)
result2=result2[result2.Channel!='507115423 1 kWh']
result2=result2[result2.Channel!='507115423 3']

result2.drop(result2.columns[3:5], axis=1,inplace=True)
result2.drop(result2.columns[0],axis=1,inplace=True)


for index,rows in result2.iterrows():

  temp=datetime.datetime.strptime(str(rows['Date']),'%Y-%m-%d %H:%M:%S').date()
  newDate=temp.strftime("%Y%m%d")
  dates=newDate
  print(dates)
  Month=str(rows['Month'])
  Day=str(rows['Day'])
  HideSpecis=1
  format=1



  url2='https://www.wunderground.com/history/airport/KBOS/2014/'+Month+'/'+Day+'/DailyHistory.html?HideSpecis=1&format=1'
  data=pd.DataFrame(pd.read_csv(url2))
  if (temp.isoweekday() in range(1, 6)):
      result2.set_value(index, 'Weekday', '1')
  else:
      result2.set_value(index, 'Weekday', '0')




  header=data.columns.values
  DewPointF=''


  timeStandard=header[0]

  if times [rows['hour']] in list(data[timeStandard]):
   TemperatureF = data.loc[data[timeStandard] == times[rows['hour']], 'TemperatureF']
   DewPointF=data.loc[data[timeStandard]==times[rows['hour']],'Dew PointF']
   Humidity= data.loc[data[timeStandard]==times[rows['hour']],'Humidity']
   SeaLevelPressure=data.loc[data[timeStandard]==times[rows['hour']],'Sea Level PressureIn']
   VisibilityMPH=data.loc[data[timeStandard]==times[rows['hour']],'VisibilityMPH']
   WindDirection=data.loc[data[timeStandard]==times[rows['hour']],'Wind Direction']
   WindSpeedMPH=data.loc[data[timeStandard]==times[rows['hour']],'Wind SpeedMPH']
   Conditions=data.loc[data[timeStandard]==times[rows['hour']],'Conditions']
   WindDirDegrees= data.loc[data[timeStandard]==times[rows['hour']],'WindDirDegrees']
   print (WindDirDegrees.iloc[0])
   result2.set_value(index, 'Temperature', str(TemperatureF.iloc[0]))
   result2.set_value(index,'Dew_PointF',str(DewPointF.iloc[0]))
   result2.set_value(index, 'Humidity',str(Humidity.iloc[0]))
   result2.set_value(index, 'Sea_Level_PressureIn',str(SeaLevelPressure.iloc[0]))
   result2.set_value(index, 'VisibilityMPH', str(VisibilityMPH.iloc[0]))
   result2.set_value(index, 'WIND_Direction',str(WindDirection.iloc[0]) )
   result2.set_value(index, 'Wind_SpeedMPH', str(WindSpeedMPH.iloc[0]))
   result2.set_value(index, 'Conditions', str(Conditions.iloc[0]))
   result2.set_value(index, 'WindDirDegress',str(WindDirDegrees.iloc[0]))

result2=result2[['Account','Date','kwh','Month','Day','Year','hour','Day of Week','Weekday','peakHour','Temperature','Dew_PointF','Humidity','Sea_Level_PressureIn','VisibilityMPH','WIND_Direction','Wind_SpeedMPH','Conditions','WindDirDegress']]
pd.DataFrame(result2).to_csv("Next6Months_10_26_2016.csv", sep=',')
fResult=result.append(result2)

pd.DataFrame(fResult).to_csv("AllRecords_New.csv", sep=',')
