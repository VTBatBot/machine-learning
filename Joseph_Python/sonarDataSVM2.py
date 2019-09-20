# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:37:01 2019

@author: Joseph
"""
#Classification Template
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os #in case of issues
from sklearn.cross_validation import StratifiedKFold 
#import the dataset
os.chdir('I:\ML_TUTORIAL\Kernel_SVM') #in case of issues
dataset = pd.read_csv('cube3438_btnrm_stc.csv')
X = dataset.iloc[:, :-1].values
#X = dataset.iloc[:, [12,15,16]].values
#X = dataset.iloc[:, [11,15,16,35,53,99]].values
#X = dataset.iloc[:, [1,12,13,15,16,21,27,28,29,34,35,38,39,41,45,51,56,72,74,87]].values
#X = dataset.iloc[:,[2,18,29,33,42,45,59,61,69,72,96,98]].values
#X = dataset.iloc[:,[7,15,16,19,100]].values
#X = dataset.iloc[:, [1,2,4,5,6,7,8,9,10,11,12,14,16,17,19,21,22,23,24,25,26,29,30,33,34,35,36,37,38,39,42,43,45,46,47,49,50,54,
#                     58,59,66,68,69,70,71,72,74,76,78,79,81,82,83,85,86,87,91,92,95,96,97,100]].values
#X = dataset.iloc[:,[3,6,8,11,12,16,17,19,22,28,29,30,35,38,43,50,53,54,55,66,68,71,78,79,81,82,85,90,95,98,99,100]].values
#X = dataset.iloc[:,[1,6,8,14,18,22,29,42,49,54,61,68,71,73,79,82]].values
#X = dataset.iloc[:, [8,30,68,71,72,78,82,91]].values
#X = dataset.iloc[:,[8,22,30,71,72,85]].values
#X = dataset.iloc[:,[8,11,22,30,71]].values
#X = dataset.iloc[:,[11,22,32,36,37,43,45,50,63,72,82,83,87,95]].values

#X = dataset.iloc[:,[16,19,22,36,41,44,45,46,50,63,72,74,75,81]].values
#X = dataset.iloc[:,[3,4,32,37,54]].values
#X = dataset.iloc[:,[1,5,11,16,22,25,32,36,37,43,45,46,50,55,58,59,63,66,72,74,79,81,82,83,85,87,95,97,98,99]].values
#X = dataset.iloc[:,[50,63,72,87]].values
#X = dataset.iloc[:,[1,3,11,15,17,41,44,48,66,72]].values
#X = dataset.iloc[:,[1,3,15,17,44,48,66,72]].values
X = dataset.iloc[:,[16,19,22,39,41,44,45,46,50,63,72,74,75,81,100]].values
#Y = dataset.iloc[:, 101].values.astype(np.float)

#Splitting the dataset into training and testing dataset

#If enough samples
from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 0)

#Feature scaling: needed for SVR

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

#X, y = make_classification(n_samples=1000, n_features=25, n_informative=10,
#                           n_redundant=2, n_repeated=0, n_classes=2,
#                           n_clusters_per_class=1, random_state=0)
#creating/fitting classifier to training set
from sklearn.svm import SVC

classifier = SVC(kernel="linear")
rfecv = RFECV(estimator = classifier, step = 1, cv=5,
              scoring = 'accuracy')
rfecv.fit(X_train,Y_train)
#print(len(cv.vocabulary_))
print("Optimal number of features : %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()
#plot_coefficients(classifier, cv.get_feature_names())
#Predicting the test ste results
y_pred = rfecv.predict(X_test)
#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

idx = np.where(rfecv.support_==True);

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