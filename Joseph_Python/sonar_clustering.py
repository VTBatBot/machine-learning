# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:25:14 2019

@author: Joseph
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os #in case of issues

#8,22,30,71,72
os.chdir('I:\ML_TUTORIAL\Kernel_SVM') #in case of issues
dataset = pd.read_csv('disc_btnrm.csv')
X = dataset.iloc[0:1000, [71,22]].values

dataset = pd.read_csv('cube_btnrm.csv')
Y = dataset.iloc[0:1000, [8,22]].values

dataset = pd.read_csv('sphere_btnrm.csv')
Z = dataset.iloc[0:1000, [8,22]].values

dataset = pd.read_csv('cyl_btnrm.csv')
M = dataset.iloc[0:1000, [8,22]].values
F = dataset.iloc[1000:2000, [8,22]].values
tot = np.vstack((X,Y,Z,M,F))

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(tot)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(tot)

plt.scatter(tot[y_kmeans == 0, 0], tot[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(tot[y_kmeans == 1, 0], tot[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(tot[y_kmeans == 2, 0], tot[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(tot[y_kmeans == 3, 0], tot[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(tot[y_kmeans == 4, 0], tot[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('autocorrelation coefficients')
plt.xlabel('2')
plt.ylabel('1')
plt.legend()
plt.show()