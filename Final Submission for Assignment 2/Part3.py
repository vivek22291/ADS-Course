import pandas as pd
import numpy as np
import datetime
import urllib.request as ur
import urllib.parse as parse
import pandas as pd

from pandas import DataFrame,read_csv
st=pd.DataFrame(read_csv("C:\\Users\\kalli\\OneDrive\\Documents\\ADS\\forecastData.csv",sep=','))
print(list(st.columns.values))
newDF=pd.DataFrame()
for index,rows in st.iterrows():
 date=datetime.datetime.strptime(str(rows['Time']),'%Y-%m-%d %H:%M:%S')
 st.set_value(index,'Date',str(date.date()))
 st.set_value(index, 'Time', str(date.time()))
 if (date.isoweekday()in range(1,6)):
  st.set_value(index, 'Weekday','1')
 else:
  st.set_value(index, 'Weekday', '0')
 times = datetime.datetime.strptime(str(date.time()), '%H:%M:%S')
 st.set_value(index,'hour',times.hour)
st['Date']=pd.to_datetime(st['Date'])
st['month'],st['day'],st['year'], st['Day of Week'] = st['Date'].dt.month, st['Date'].dt.day,st['Date'].dt.year,(st['Date'].dt.dayofweek+1)%7
peakIndicator = ((7<=st['hour']) & (st['hour']<=19))
st['PeakHour']=np.where(peakIndicator,1,0)
print(st)


st=st[['Date','month','day','year','hour','Day of Week','Weekday','PeakHour','TemperatureF','Dew_PointF','Humidity','Sea_Level_PressureIn','VisibilityMPH','Wind_Direction','Wind_SpeedMPH','Conditions','WindDirDegrees']]


pd.DataFrame(st).to_csv("File7.csv", sep=',')