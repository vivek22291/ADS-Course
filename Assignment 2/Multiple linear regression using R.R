library(MASS)
library(ISLR)
library(car)
install.packages('forecast')
library(forecast)
install.packages("leaps")
library(leaps)

df <- read.csv(file="C:\\Users\\Vivek\\Desktop\\ADS\\Assignments\\ADS-Course\\Assignment 2\\WeatherTest.csv", header=TRUE, sep=",")
#names(df)
# print(df)

#75% of the sample size
smp_size <- floor(0.75 * nrow(df))

#Set the seed to make your partition reproductible
set.seed(123)
train_ind <- sample(seq_len(nrow(df)), size = smp_size)

#Split the data into training and testing
train <- df[train_ind, ]
test <- df[-train_ind, ]

lm.fit=lm(kWh~ ., data=train)
summary(lm.fit)

# lm.fit$coefficients
# lm.fit[[1]]
# confint(lm.fit, level = 0.95)
# summary(lm.fit)$coefficients

#Measures of predictive accuracy

# head(df)
# head(train)

df = na.omit(df)

##### Searching all subset models up to size 8 by default
regfit.full=regsubsets(khw~.-Account - Date - ,data=df)
summary(regfit.full)

##### Searching all subset models up to size number of variables
regfit.full=regsubsets (Sales~.,data=Carseats ,nvmax=11) 
reg.summary =summary (regfit.full)
names(reg.summary)
reg.summary$rss
reg.summary$adjr2

## Plotting and choosing the subset
par(mfrow=c(2,2)) 
plot(reg.summary$rss ,xlab="Number of Variables ",ylab="RSS", type="l") 
plot(reg.summary$adjr2 ,xlab="Number of Variables ", ylab="Adjusted RSq",type="l")
coef(regfit.full ,6)


#### Forward selection
regfit.fwd=regsubsets(Sales~.,data=Carseats ,nvmax=11, method="forward") 
F=summary(regfit.fwd)
names(F)
F
F$rss
F$adjr2
coef(regfit.fwd,6)

#### Backward selection
regfit.bwd=regsubsets(Sales~.,data=Carseats ,nvmax=11, method="backward") 
B=summary(regfit.bwd)
names(B)
B
B$rss
B$adjr2
