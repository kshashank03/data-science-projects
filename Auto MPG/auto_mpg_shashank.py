#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:39:24 2019

@author: shashankkalanithi
"""

import numpy as np
import matplotlib as plt
import pandas as pd
from patsy import dmatrices

#Import and clean data
filepath = "/Users/shashankkalanithi/Documents/Data Science/Machine Learning Projects/Auto MPG/auto-mpg.xlsx"
dataset = pd.read_excel('auto-mpg.xlsx')
indexNames = dataset[ dataset['horsepower'] == '?'].index
dataset.drop(indexNames, inplace =True)
dataset.drop(['horsepower'], axis=1)

#Tried to change datatypes wasn't necessary
'''dataset.astype({'cylinders': 'float64'}).dtypes
dataset.astype({'displacement': 'float64'}).dtypes
dataset.astype({'weight': 'float64'}).dtypes
dataset.astype({'acceleration': 'float64'}).dtypes
dataset.astype({'model_year': 'float64'}).dtypes
dataset.astype({'mpg': 'float64'}).dtypes'''

#This was to clean the horsepower column, just ended up dropping the feature
'''print("Dropped rows:")
print(indexNames)'''

X = dataset.iloc[:, 1:6].values
y = dataset.iloc[:, 0:1].values

#Split data, train, test, and fit models
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

#Use Backwards Elimination to determine which variables are significant
import statsmodels.api as sm
X = np.append(arr = np.ones((392, 1)).astype(int), values = X, axis = 1)
y_matrix, X_matrix = dmatrices('mpg ~ cylinders + displacement + weight + acceleration + model_year', data=dataset, return_type='dataframe')

#Testing all variables (except horsepower)
X_opt = X_matrix.iloc[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y_matrix, exog = X_opt).fit()
regressor_OLS.summary()
#Testing w/o cylinders
X_opt = X_matrix.iloc[:, [0, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y_matrix, exog = X_opt).fit()
regressor_OLS.summary()
#Testing w/o cylinders or displacement
X_opt = X_matrix.iloc[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y_matrix, exog = X_opt).fit()
regressor_OLS.summary()
#Testing w/o cylinders or displacement or acceleration
X_opt = X_matrix.iloc[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y_matrix, exog = X_opt).fit()
regressor_OLS.summary()