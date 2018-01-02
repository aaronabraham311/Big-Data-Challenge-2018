library(tidyverse)
library(caret)
library(randomForest)

allData <- read.csv("/Users/aaronabraham/Documents/Programming/Python/BDC/BDC-AK/data/processed/cleaned.csv")
allData <- subset(allData, select = -c(1))
set.seed(40)

indices <- createDataPartition(allData$ViolentCrimesPerPop., p = 0.7, list = FALSE) #70% of data will be for training
train <- allData[indices,]
test <- allData[-indices,]

# Randomizing training:
train <- train[sample(nrow(train)),]

controlParameters <- trainControl(
  method = "cv",
  number = 10, 
  savePrediction = TRUE,
  classProbs = TRUE
)


# Linear Regression
linModel <- train(ViolentCrimesPerPop. ~ .,
                  data = train,
                  method = "lm",
                  trControl = controlParameters)
linPredictions <- predict(linModel, test)
modelValues<-data.frame(obs = test$ViolentCrimesPerPop., pred=linPredictions)
defaultSummary(modelValues) # RMSE: 0.1450994. r2 : 0.6556255

linVariableImportance <- varImp(linModel)
plot(linVariableImportance)

# Stepwise regression
stepModel <- train(ViolentCrimesPerPop. ~ .,
                  data = train,
                  method = "glmStepAIC",
                  trControl = controlParameters)
stepPredictions <- predict(stepModel, test)
stepModelValues<-data.frame(obs = test$ViolentCrimesPerPop., pred=stepPredictions)
defaultSummary(stepModelValues) # RMSE: 0.1455873. r2 : 0.6533207

stepVariableImportance <- varImp(stepModel)
plot(stepVariableImportance)

# Relaxed LASSO
relaxoModel <- train(ViolentCrimesPerPop. ~ .,
                   data = train,
                   method = "relaxo",
                   trControl = controlParameters) #Justification: https://stats.stackexchange.com/questions/88466/how-to-select-tuning-parameter-for-regularized-regressions-for-interpretation
relaxoModel <- readRDS("relaxo_model.RDS")

relaxoPredictions <- predict(relaxoModel, test)
relaxoModelValues<-data.frame(obs = test$ViolentCrimesPerPop., pred=relaxoPredictions)
defaultSummary(relaxoModelValues) #RMSE: 0.703378. r2: E

relaxoVariableImportance <- varImp(relaxoModel)
plot(relaxoVariableImportance)

# Extreme gradient boosting https://stats.stackexchange.com/questions/278747/how-does-xgboost-do-regression-using-trees
plsModel <- train(ViolentCrimesPerPop. ~ .,
                  data = train,
                  method = "xgbTree",
                  trControl = controlParameters)
xgbModel <- plsModel
# xgbModel <- readRDS("xgb_model.RDS")

xgbPredictions <- predict(xgbModel, test)
xgbModelValues<-data.frame(obs = test$ViolentCrimesPerPop., pred=xgbPredictions)
defaultSummary(xgbModelValues) #RMSE: 0.13652815. r2: 0.64856267

xgbVariableImportance <- varImp(xgbModel)
plot(xgbVariableImportance)

# Random forest model
rfModel <- randomForest(ViolentCrimesPerPop. ~ .,
                        data = train,
                        importance = TRUE)
#rfModel <- readRDS("rf_model.RDS")

rfPredictions <- predict(rfModel, test)
rmse = sqrt(mean((test$ViolentCrimesPerPop.-rfPredictions)^2)) #0.1351691

#ENSEMBLING:
