#installing libraries
#install_packages("caTools")
#install_packages("ggplot2")

#importing libraries
library(caTools)
library(ggplot2)

#importing data
dataset <- read.csv("/Users/DK/Documents/Machine_Learning/R/Side_Projects/Linear_Regression/Salary_data.csv")

#test and training sets
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 0.8)
training_set <- subset(dataset,split = TRUE)
test_set <- subset(dataset,split = FALSE)

#feature scaling
#training_set[,1:2] <- scale(training_set[,1:2])
#test_set[,1:2] <- scale(test_set[,1:2])

#linear regression model
lin_reg <- lm(Salary~YearsExperience,data=dataset)
y_pred <- predict(lin_reg,test_set)

#visualisation of training_set
ggplot() + 
geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary,color="red")) + 
geom_line(aes(x=training_set$YearsExperience,predict(lin_reg,training_set),color="blue")) +
ggtitle("Salary vs Years of Experience (Training Set)") +
xlab("YearsExperience") +
ylab("Salary")

#visualisation of test_set
ggplot() +
geom_point(aes(x=test_set$YearsExperience,y=test_set$Salary,color="red")) +
geom_line(aes(x=test_set$YearsExperience,y_pred,color="blue")) +
ggtitle("Salary vs Years of Experience") +
xlab("YearsExperience") +
ylab("Salary")






