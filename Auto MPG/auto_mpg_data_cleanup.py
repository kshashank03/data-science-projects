#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:59:08 2019

@author: shashankkalanithi
"""
#Import the necessary packages
import pandas as pd

#Import our dataset
dataset = pd.read_excel("auto-mpg.xlsx")

#Clean the horsepower column

#Index the columns that have a horsepower value unfilled
indices_to_drop = dataset[dataset['horsepower'] == '?'].index.tolist()
dataset = dataset.drop(dataset.index[indices_to_drop])
dataset.dtypes
dataset["horsepower"] = pd.to_numeric(dataset["horsepower"])
dataset.dtypes

#Encoding our car model categorical variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()
dataset_le = dataset
dataset_le.car = le.fit_transform(dataset_le.car)
X = dataset.iloc[:, 1:]
y = dataset.iloc[:, 0:1]
X_array = X.values
y_array = y.values
ohe = OneHotEncoder(categorical_features=[7])
X_array = ohe.fit_transform(X_array).toarray()
