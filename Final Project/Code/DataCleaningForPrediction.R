library(jsonlite)
library(rjson)
library(plyr)
library(tidyr)
library ()

library('dplyr')

library('chron')
library('lubridate')
library("rvest")
library("ggmap")
library("rwunderground")
library("weatherData")
library("XML")
library("geosphere")
library("sklearn")
library("rPython")
library("knitr")
install.packages("sklearn")
install.packages("Python")
install.packages("knitr")
install.packages("rmarkdown")






#Extracting values from a JSON File
data<-fromJSON(file="C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\yelp_academic_dataset_Business.json",method="C")
data<-lapply(data,function(d)
{
  d[sapply(d,is.null)]<-NA
  unlist(d)
})
do.call("rbind",data)

data<-ldply(data,rbind)

print()
write.csv(data,file='Business.csv')



#Garbage Collector
gc()
business2<-business
businessSample2<-sampleBusiness

business<-read.csv("C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\Business.csv")

business1<-read.csv("C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\Business.csv")
checkin<-read.csv("C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\Checkin.csv")
review<-read.csv("C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\review.csv")
tip<-read.csv("C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\tip.csv")
user<-read.csv("C:\\Users\\kalli\\OneDrive\\Documents\\DataScienceFinals\\user.csv")
review_new<-review[sample(nrow(review),50000),]
tip_new<-tip[sample(nrow(tip),50000),]
user_new<-user[sample(nrow(user),50000),]
colnames(third_merge)
write.csv(review_new,file="New_Review.csv")





for(i in c(1,1:111)){
  
  if (class(business[,i])=='logical')
  {
    
    business[,i] <- as.numeric(business[,i])
   
  }
}

#Replacing blanks with NA
for(i in c(1,1:112)){
  
  
    business[,i][is.na(business[,i])] <- 'NA'
  
}

business<-business[c(1,2,3,60,15,16,62,65,66,88,89,101,111,112,4,5,6,7,8,9,10,11,12,13,14,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112)]

business<-gather (business,"Category","Category.Value",4:14)



#Check for US States and drop those which are not US states
dats<-read_html("http://www.stateabbreviations.us/")
stateTable<-as.data.frame(dats%>%html_nodes("table")%>%.[[2]]%>%html_table())

#Filter out some rows
stateTable<-stateTable[,-c(1,2,4)]
stateTable<-as.data.frame(stateTable)
business$state<-as.character(business$state)
class(stateTable$stateTable)
class(business$state)
stateTable$stateTable<-as.character(stateTable$stateTable)
business$state[!(business$state%in%stateTable$stateTable)]<-1
business<-business[!business$state==1,]
summary(business$attributes.Good.For.breakfast)
unique(business$state)

business<-business[order(business$X),]
business<-business[,-c(111)]
business[,111][is.na(business[,111])] <- 'NA'
business<-business[!business$Category.Value=='NA',]
business<-business[business$Category.Value=='Restaurants',]
business<-business[order(business$state,business$city),]
print(business$Category.Value)
summary(business$attributes.Alcohol)




#Remove Unnecesaary Features
business<-business[,-c(109,110,108,107,106,104,105,103,101,102,99,100,98,97,96,95,93,94,91,92,89,90,87,88,85,86,83,84,81,82,80,79,77,78,74)]


business<-business[,-(4:13)]
business<-business[,-(51:52)]
business<-business[,-(58:59)]
business<-business[,-62]
business<-business[,-(50:52)]
business<-business[,-48]

business<-business[c(1,2,3,4,5,6,7,8,9,10,11,47,21,40,41,52,46,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,48,49,50,51,53,54,55,56,57)]
business<-business[1:12736,]
business<-business[c(1,2,3,5,6,7,8,9,10,11,12,13,28,54,56,16,17,4,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,57,58,59)]



temp<-aggregate(attributes.Good.For.dessert ~ city, data = business,count)

#Function to find Mode of columns per city

findMode <- function(m) {
  removedValues <- na.omit(unique(m))

  removedValues[which.max(tabulate(match(m, removedValues)))]
}
rm(dataCleaning)


#Cleaning range of Rows and creating a new Data frame for Comparison
for (l in 22:60  )
{
dataCleaning<-cbind(sample,setNames(aggregate(business[,l],list(business$city), findMode),c(colnames(business)[4],colnames(business)[l])))
}

dataCleaning<-dataCleaning[c(1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84)]




for (i in 1:nrow(dataCleaning))
{
  for (y in 2:ncol(dataCleaning) )
    {
    if (lengths(dataCleaning[i,y])>=2)
    {
    dataCleaning[i,y]<-TRUE
    }
    if (is.na(dataCleaning[i,y]))
    {
      dataCleaning[i,y]<-FALSE
    }
  }
}

dataCleaning<-dataCleaning[,-c(3,4)]


for (y in 2:ncol(dataCleaning))
{
  dataCleaning[,y]<-as.logical(dataCleaning[,y])
}

#Create a copy of the Business Data set to work on
sampleBusiness<-business


#Compare values with sampleBusiness data frame and fill in missing NA values in the dataset
for (i in 1:nrow(sampleBusiness))
{
  for (y in 32:ncol(sampleBusiness) )
  {
    if (is.na(sampleBusiness[i,y]))
    {

      sampleBusiness[i,y]<-dataCleaning[which(dataCleaning$city == sampleBusiness[[i,4]]),which(colnames(dataCleaning)==colnames(sampleBusiness)[y])]

    }
    
  }
}


#Similarly compare values in other column with the dataCleaning dataset

for (i in 1:nrow(sampleBusiness))
{
  for (y in 22:30 )
  {
    if (is.na(sampleBusiness[i,y]))
    {
    
      sampleBusiness[i,y]<-dataCleaning[which(dataCleaning$city == sampleBusiness[[i,4]]),which(colnames(dataCleaning)==colnames(sampleBusiness)[y])]

    }
    
  }
}

sampleBusiness<-sampleBusiness[,-c(13,31)]
summary(sampleBusiness$attributes.Takes.Reservations)









sampleBusiness[is.na(sampleBusiness)]<-" "





#Save a copy of Sample Business Dataset in local

write.csv(sampleBusiness,"PartiallyCleaned2_Business_Restaurants.csv")







