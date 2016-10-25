import numpy as np
import pandas as pd
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import *


le = preprocessing.LabelEncoder()

d = pd.read_csv('C:\\Users\\Vivek\\Desktop\\ADS\\Assignments\\ADS-Course\\Assignment 2\\WeatherTest.csv', index_col=0,
                dtype={'Account': int, 'Peakhour': bool})
#print(d)
encodedWeekday = le.fit_transform(d["Weekday"])
#print(encodedWeekday)
encodedPeakHour = le.fit_transform(d["Peakhour"])
#print(encodedPeakHour)
encodedWindDirection = le.fit_transform(d["Wind_Direction"])
encodedConditions = le.fit_transform(d["Conditions"])
encodedWindDirDegrees = le.fit_transform(d["WindDirDegrees"])

#select the features
features = pd.DataFrame([encodedPeakHour, d["Dew_PointF"], d["Wind_SpeedMPH"], d["Humidity"], d["Temperature"]]).T
print(features)


X = features
y = d["kWh"]

'''
lm = linear_model.LinearRegression()
lm.fit(X, y)
print(lm.intercept_)
print(lm.coef_)
'''

#Splitting into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#print("training data is ", X_train)
#print("test data is ", X_test)

lm = linear_model.LinearRegression()
lm.fit(X_train, y_train)
trainScore = lm.score(X_train, y_train)
print("The score of train data is ", trainScore)

print("Intercept is ", lm.intercept_)
print("Coefficient/s is/are ", lm.coef_)

trainPred = lm.predict(X_train)
print("Train data performance measures")
#Rsquare score of the model
r2Score_train = r2_score(y_train, trainPred)
print("R2 score is: ", r2Score_train)

#Mean absolute error
MAE_train= mean_absolute_error(y_train, trainPred)
print("Mean Absolute Error score is: ", MAE_train)

#Mean squared error
MSE_train = mean_squared_error(y_train, trainPred)
print("Mean Squared error score is: ", MSE_train)

#Median absolute error
MeAE_train = median_absolute_error(y_train, trainPred)
print("Median Absolute Error score is: ", MeAE_train)

#Root Mean squared error
RMS_train = np.sqrt(MSE_train)
print("Root Mean Squared Error is ", RMS_train)

print("Test data performance measures")
testPred = lm.predict(X_test)

#Rsquare score of the model
r2Score_test = r2_score(y_test, testPred)
print("R2 score is: ", r2Score_test)

#Mean absolute error
MAE_test= mean_absolute_error(y_test, testPred)
print("Mean Absolute Error score is: ", MAE_test)

#Mean squared error
MSE_test = mean_squared_error(y_test, testPred)
print("Mean Squared error score is: ", MSE_test)

#Median absolute error
MeAE_test = median_absolute_error(y_test, testPred)
print("Median Absolute Error score is: ", MeAE_test)

#Root Mean squared error
RMS_test = np.sqrt(MSE_test)
print("Root Mean Squared Error is ", RMS_test)

