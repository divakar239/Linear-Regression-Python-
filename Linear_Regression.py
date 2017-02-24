#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:41:12 2017

@author: DK
"""
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

#Reading in dataset;separate the dependent and independent sets
dataset = pd.read_csv('/Users/DK/Documents/Machine_Learning/Python/Macine_Learning_Projects/Linear Regression/Salary_Data.csv');
X = dataset.iloc[:,:-1].values;    
Y = dataset.iloc[:,1].values;

#Training and test set
from sklearn.cross_validation import train_test_split;
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 1/3, random_state = 0);

#Feature Scaling
from sklearn.preprocessing import StandardScaler;
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train);
X_test = sc_X.transform(X_test);

#Linear Regression Model
from sklearn.linear_model import LinearRegression;
regressor = LinearRegression();
regressor.fit(X_train,Y_train);
Y_pred = regressor.predict(X_test);

#Visualising Training Set
plt.scatter(X_train,Y_train,color = 'red');
plt.plot(X_train,regressor.predict(X_train));
plt.title("Salary vs Experience (Training Set)");
plt.xlabel("Experience");
plt.ylabel("Salary");
plt.show();

#Visualising Test Set
plt.scatter(X_test,Y_test,color = "red");
plt.plot(X_test,Y_pred);
plt.title("Salary vs Experience");
plt.xlabel("Experience");
plt.ylabel("Salary");
plt.show();