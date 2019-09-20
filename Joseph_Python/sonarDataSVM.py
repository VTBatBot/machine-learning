# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 00:33:44 2019

@author: Joseph
"""

#Classification Template
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os #in case of issues

def plot_coefficients(classifier, feature_names, top_features = 20):
        coef = classifier.coef_.ravel()
        top_positive_coefficients = np.argsort(coef)[-top_features:]
        top_negative_coefficients = np.argsort(coef)[:top_features]
        top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
        
        plt.figure(figsize=(15,5))
        colors = ['red' if c< 0 else 'blue' for c in 
                  coef[top_coefficients]]
        plt.bar(np.arange(2*top_features, coef[top_coefficients]), color = colors)#,feature_names[top_coefficients])
        #, rotation = 60, ha='right')
        plt.show()
        
#import the dataset
os.chdir('I:\ML_TUTORIAL\Kernel_SVM') #in case of issues
dataset = pd.read_csv('cube_between_stc24_28.csv')
#X = dataset.iloc[:, :-1].values
#X = dataset.iloc[:, [0,9,68]].values
#X = dataset.iloc[:, [0,9,11,66,67,68]].values
#X = dataset.iloc[:, [0,9,10,11,12,13,15,16,17,18,19,1,21,2,3,73,74,75,76,77,78,61,79,62,63,64,65,66,67,68]].values

X = dataset.iloc[:, :-2].values
Y = dataset.iloc[:, 101].values.astype(np.float)

#Splitting the dataset into training and testing dataset

#If enough samples
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 0)

#Feature scaling: needed for SVR

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)


#creating/fitting classifier to training set
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer

classifier = LinearSVC()
classifier.fit(X_train, Y_train)
cv = CountVectorizer()
cv.fit(dataset)
#print(len(cv.vocabulary_))
print(cv.get_feature_names())
#plot_coefficients(classifier, cv.get_feature_names())
#Predicting the test ste results
y_pred = classifier.predict(X_test)
#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

#Visualizing the training set results
"""
from matplotlib.colors import ListedColormap
X_set, Y_set = X_train, Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test Set)')
plt.xlabel('Age [scaled years]')
plt.ylabel('Estimiated Salary [scaled $]')
plt.legend()
plt.show()
                                
"""