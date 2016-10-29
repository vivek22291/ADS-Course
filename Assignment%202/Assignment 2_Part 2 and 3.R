library(MASS)
library(ISLR)
install.packages('forecast')
library(forecast)
install.packages("leaps")
library(leaps)
install.packages("xlsx", dependencies = TRUE)
library(xlsx)


options(max.print=1000000)

#Read the CSV File
df <- read.csv(file="sampleformat.csv", header=TRUE, sep=",")
summary(df)
df = na.omit(df)
df <- df[ -c(1, 2, 16, 17, 18)]
          
#Divide the data set into train and test
#75% of the sample size
smp_size <- floor(0.75 * nrow(df))

#Set the seed to make your partition reproductible
set.seed(1000)
train_ind <- sample(seq_len(nrow(df)), size = smp_size)

#Split the data into training and testing
train <- df[train_ind, ]
test <- df[-train_ind, ]


##### Searching all subset models up to size number of variables
regfit.full=regsubsets (kWh~.,data=train ,nvmax=11)
reg.summary =summary (regfit.full)
names(reg.summary)
reg.summary$rss
reg.summary$adjr2


par(mfrow=c(2,2))
plot(reg.summary$rss ,xlab="Number of Variables ",ylab="RSS", type="l")
plot(reg.summary$adjr2 ,xlab="Number of Variables ", ylab="Adjusted RSq",type="l")
coef(regfit.full ,6)

#### Forward selection
regfit.fwd=regsubsets(kWh~ ., data=train ,nvmax=11, method="forward")
F=summary(regfit.fwd)
names(F)
F
F$rss
F$adjr2
coef(regfit.fwd,6)

#### Backward selection
regfit.bwd=regsubsets(kWh~ .,data=train ,nvmax=11, method="backward")
B=summary(regfit.bwd)
names(B)
B
B$rss
B$adjr2
coef(regfit.bwd,6)

#Exhaustive Search
leaps=regsubsets(kWh~.,data=train, nbest=12)
plot(leaps, scale="adjr2")
plot(leaps, scale="bic")

null=lm(kWh~1, data=df)
null

full=lm(kWh~., data=df)
full
step(null, scope=list(lower=null, upper=full),data = df, direction="forward")
step(null, scope=list(lower=null, upper=full),data = df, direction="backward")
step(null, scope=list(lower=null, upper=full),data = df, direction="both")



#implement linear multiple regression using different predictors 
lm.fit=lm(kWh~ ., data=train)  #all columns
summary(lm.fit)
lm.fit<-lm(kWh ~ Day+peakHour+Month+Temperature+Day.of.Week+Weekday, data = train)
lm.fit<-lm(kWh ~ Month+Day+hour+peakHour+Sea_Level_PressureIn+Weekday+Day.of.Week,data = train) #Multiple R-squared:  0.511,	Adjusted R-squared:  0.5105
lm.fit=lm(kWh ~ Month + Day + Weekday + peakHour + Dew_PointF + Humidity, data = train) #Multiple R-squared:  0.5309,	Adjusted R-squared:  0.5304 
lm.fit<-lm(kWh ~ Month+Day+hour+Dew_PointF + Humidity + Sea_Level_PressureIn + VisibylityMPH,data = train) #Multiple R-squared:  0.05617,	Adjusted R-squared:  0.05515 
lm.fit<-lm(kWh ~ Month+Day+hour+peakHour+Temperature+Weekday+Day.of.Week+Wind_SpeedMPH, data = train) #Multiple R-squared:  0.05617,	Adjusted R-squared:  0.05515 
lm.fit<-lm(kWh ~ Day+Temperature+Humidity+peakHour+Weekday+Month+Day.of.Week,data = train)
lm.fit<-lm(kWh ~ Dew_PointF + hour + Day + Temperature + Humidity + peakHour + Weekday + Month + Day.of.Week, data = train) #Multiple R-squared:  0.5688,	Adjusted R-squared:  0.5682
summary(lm.fit)


#Export the regression outputs to external file
regressionOutput <- summary(lm.fit)$coefficients
write.xlsx(regressionOutput, "Regression_Coefficients.xlsx")
regressionCoefficients_df <- read.xlsx("Regression_Coefficients.xlsx", sheetIndex = 1)
regressionOutput_df <- regressionCoefficients_df[ -c(2,3,5)]
unlink("Regression_Coefficients.xlsx", recursive = FALSE, force = FALSE)
write.csv(regressionOutput_df, "RegressionOutputs.csv")

#Predict the test data
pred = predict(lm.fit, test)
testDataAccuracy <- accuracy(pred, train$kWh)

#Export Perforance matrix of model to external file
write.csv(testDataAccuracy, "PerformanceMatrix.csv")


#Part 3: Forecasting
#read the forecasting data by importing it
predictionInput <- read.csv(file="forecastData.csv", header=TRUE, sep=",")

#cleaning the data
predictionInput = na.omit(predictionInput)
colnames(predictionInput)[4] <- "Day"
colnames(predictionInput)[10] <- "Temperature"
colnames(predictionInput)[9] <- "peakHour"
colnames(predictionInput)[3] <- "Month"
summary(predictionInput)
predictionInput <- predictionInput[ -c(1, 2, 15, 16, 17)]

#Forecasting for the newdata using data from forecastInput
predict1 = predict(lm.fit, newdata = predictionInput)
summary(predict1)

#extract the required columns 
predictionOutput <- predictionInput
predictionOutput["kWh"] <- predict1
predictionOutput$date <- as.Date(with(predictionOutput, paste(year, Month, Day,sep="-")), "%Y-%m-%d")
forecastOutput <- predictionOutput[-c(1:3, 5:7, 9:13)]
forecastOutput <- forecastOutput[c(4,1,2,3)]
summary(forecastOutput)

#Export forecasted data to external file
write.csv(forecastOutput, "forecastOutput_Account_26908650026.csv ")




