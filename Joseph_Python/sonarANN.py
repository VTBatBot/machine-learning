# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:46:59 2019

@author: Joseph
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import keras

import math

data = np.loadtxt('dataset_stc6161f.dat')
X = data[0:400,0:250]
y = data[0:400,-1]
#y = keras.utils.to_categorical(y, num_classes=5)

X_test = X
y_test = y

data_train = np.loadtxt('datasetx_og61.dat')
X_train = data_train[:,0:250]
y_train = data_train[:,-1]
"""
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
"""
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from keras.models import Sequential
from keras.layers import Dense


classifier = Sequential()
classifier.add(Dense(output_dim = 25, kernel_initializer= 'uniform', activation= 'relu', input_dim = 250))
classifier.add(Dense(output_dim = 25, kernel_initializer= 'uniform', activation= 'relu'))
classifier.add(Dense(output_dim = 25, kernel_initializer= 'uniform', activation= 'relu'))
classifier.add(Dense(output_dim = 25, kernel_initializer= 'uniform', activation= 'relu'))
classifier.add(Dense(output_dim = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss= 'binary_crossentropy', metrics = ['accuracy'])
classifier.fit(X_train, y_train, batch_size=10, epochs = 100)
"""
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.2)
classifier.summary()
"""
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
