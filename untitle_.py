# -*- coding: utf-8 -*-
"""untitle .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQJi5ekj5Y1p3XV87RA-6fCd2oZEAOV4

Find Mean Median Mode of Dataset
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('SOCR-HeightWeight.csv')
df.head()

df.info()

df.isnull().sum()

df.shape

df.isnull().sum()

data = df.iloc[:, 1]
data

mean = data.mean()
mean

plt.figure(figsize=(12,8))
plt.hist(data, bins=25, edgecolor = 'black', alpha = 0.6 , color = '#e06666')
plt.axvline(mean, color='purple',lw=3, label=f'Mean: {mean}')
plt.xlabel('Height(Inches)')
plt.ylabel('Count')
plt.title('Mean of Heights', fontsize=16)
plt.legend()

median = data.median()
median

plt.figure(figsize=(12,8))
plt.hist(data, bins=25, edgecolor = 'black', alpha = 0.6 , color = '#e06666')
plt.axvline(mean, color='brown',lw=3, label=f'Median: {median}')
plt.xlabel('Height(Inches)')
plt.ylabel('Count')
plt.title('Median of Heights', fontsize=16)
plt.legend()

mode = data.mode()
modeList = mode.to_list()
mode

plt.figure(figsize=(12,8))
plt.hist(data, bins=25, edgecolor = 'black', alpha = 0.6 , color = '#e06666')

for i in range(0,len(modeList)):
  plt.axvline(modeList[i], color='green',lw=1, label=f'Mode {i}: {modeList[i]}')

plt.xlabel('Height(Inches)')
plt.ylabel('Count')
plt.title('Mode of Heights', fontsize=16)
plt.legend()

"""Implement box plot from dataset"""

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.normal(size=100)

# Create box plot
fig, ax = plt.subplots()
ax.boxplot(data)

# Add title and axis labels
ax.set_title('Box plot of sample data')
ax.set_xlabel('Data')
ax.set_ylabel('Value')

# Show plot
plt.show()

"""Implement box plot from dataset & replace outlier by interquartile range"""

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.normal(size=1000)

# Create box plot
fig, ax = plt.subplots()
ax.boxplot(data)

# Calculate interquartile range (IQR)
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1

# Identify outliers based on IQR
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
outliers = np.where((data < lower_bound) | (data > upper_bound))

# Replace outliers with IQR
data[outliers] = np.median(data)

# Create box plot with outliers replaced by IQR
fig2, ax2 = plt.subplots()
ax2.boxplot(data)

"""Implement heatmap & find the features whose threshold is greater than 0.7"""

import numpy as np
import matplotlib.pyplot as plt

# Generate random matrix
data = np.random.rand(10, 10)

# Create heatmap
plt.imshow(data, cmap='coolwarm')

# Show colorbar
plt.colorbar()

# Show plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate random matrix
data = np.random.rand(10, 10)

# Create heatmap
plt.imshow(data, cmap='coolwarm')

# Show colorbar
plt.colorbar()

# Find values greater than 0.7
for i in range(10):
    for j in range(10):
        if data[i][j] > 0.7:
            plt.text(j, i, "{:.2f}".format(data[i][j]), ha="center", va="center", color="w")

# Show plot
plt.show()

"""# New Section

Apply Oversampling Smote Technique using csv
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
import statistics

data = pd.read_csv("winequality-red.csv")

data.head()

data.shape

data.columns

data.describe()

data["quality"].value_counts()

data.isnull().any()

data.info()

data['goodquality'] = [1 if x >= 5 else 0 for x in data['quality']]

data['goodquality'].value_counts()

# Separate feature variables and target variable
features = data.drop(['quality','goodquality'], axis = 1)
target = data['goodquality']

# Normalize feature variables
from sklearn.preprocessing import StandardScaler
x_features = features
feature_attr = StandardScaler().fit_transform(x_features)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(feature_attr,target, train_size = 0.80, random_state = 25)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

print("Before OverSampling, counts of label '1': {}".format(sum(y_train == 1)))
print("Before OverSampling, counts of label '0': {} \n".format(sum(y_train == 0)))

from collections import Counter
minority_class = min(Counter(y_train), key=Counter(y_train).get)

# Calculate the number of samples needed to balance the classes
num_minority_samples = Counter(y_train)[minority_class]
num_majority_samples = Counter(y_train)[max(Counter(y_train), key=Counter(y_train).get)]
num_synthetic_samples = num_majority_samples - num_minority_samples

from imblearn.over_sampling import SMOTE

# Apply SMOTE to the training set
smote = SMOTE(sampling_strategy='minority')
x_train_resampled, y_train_resampled = smote.fit_resample(x_train, y_train)

from sklearn.ensemble import RandomForestClassifier
# Train a Random Forest classifier on the resampled training set
clf = RandomForestClassifier(random_state=42)
clf.fit(x_train_resampled, y_train_resampled)

from sklearn.metrics import classification_report, roc_curve

# Evaluate the model on the testing set
y_pred = clf.predict(x_test)
print(classification_report(y_test, y_pred))

from sklearn import metrics
y_pred_proba = clf.predict_proba(x_test)[::,1]
fpr,tpr,_ = roc_curve(y_test, y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True positive rate')
plt.xlabel('False positive rate')
plt.legend(loc=4)
plt.show()

"""Apply KNN method to detect outlier"""

# import libraries
#import the pandas library and aliasing as pd
import pandas as pd
import pandas as pd
df = pd.DataFrame()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

data = pd.read_csv("Iris.csv")
# input data
df = data[["SepalWidthCm", "PetalLengthCm"]]

plt.scatter(df["SepalWidthCm"], df["PetalLengthCm"])

# create arrays
X = df.values

# instantiate model
nbrs = NearestNeighbors(n_neighbors = 3)
# fit model
nbrs.fit(X)

# distances and indexes of k-neaighbors from model outputs
distances, indexes = nbrs.kneighbors(X)
# plot mean of k-distances of each observation
plt.plot(distances.mean(axis =1))

# visually determine cutoff values > 0.15
outlier_index = np.where(distances.mean(axis = 1) > 0.15)
outlier_index

# filter outlier values
outlier_values = df.iloc[outlier_index]
outlier_values

# plot data
plt.scatter(df["SepalWidthCm"], df["PetalLengthCm"], color = "b", s = 65)
# plot outlier values
plt.scatter(outlier_values["SepalWidthCm"], outlier_values["PetalLengthCm"], color = "r")

"""Plot the scatter plot."""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df1 = pd.read_csv('SOCR-HeightWeight.csv')
df1.head()

df.info()

df.isnull().sum()

df.mean(axis=0)

plt.figure(figsize=(12,8))
sns.scatterplot(x=df1['Height(Inches)'], y=df1['Weight(Pounds)'])

"""Perform T-test by considering any hypothesis"""

ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]

len(ages)

import numpy as np
ages_mean=np.mean(ages)
print(ages_mean)

std = np.std(ages)
print("Standard Deviation:", std)

## Lets take sample

sample_size=10
age_sample=np.random.choice(ages,sample_size)

age_sample

from scipy.stats import ttest_1samp

ttest,p_value=ttest_1samp(age_sample,30)

print(p_value)

if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")

"""Perform Z-test by considering any hypothesis."""

import scipy.stats as st
Mu = ages_mean
Std = std

sample_avg_bp = np.average(ages)
std_error_bp = Std / np.sqrt(len(ages)) # Standard dev of the sampling mean distribution... estimated from population
print("Sample Avg BP : " , sample_avg_bp)
print("Standard Error: " , std_error_bp)

# Z_norm_deviate =  sample_mean - population_mean / std_error_bp

Z_norm_deviate = (sample_avg_bp - Mu) / std_error_bp
print("Normal Deviate Z value :" , Z_norm_deviate)

p_value = st.norm.sf(abs(Z_norm_deviate))*2 #twosided using sf - Survival Function
print('p values' , p_value)

if p_value > 0.05:
  print('Samples are likely drawn from the same distributions (H0 accepted)')
else:
  print('Samples are likely drawn from different distributions (reject H0)')

"""Apply Oversampling SMOTE Technique. example 2

"""

import pandas as pd
from sklearn.datasets import load_breast_cancer
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.head()

sns.countplot(x="target", data = df)

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LogisticRegression(max_iter=10000)
lr.fit(X_train, y_train)
y_pred_normal = lr.predict(X_test)

cm_normal = confusion_matrix(y_test, y_pred_normal)
print('Confusion matrix (Normal Logistic Regression):\n')
print(cm_normal)
print('\nClassification report (Normal Logistic Regression):\n')
print(classification_report(y_test, y_pred_normal))

rus = RandomUnderSampler(random_state=42)
X_train_under, y_train_under = rus.fit_resample(X_train, y_train)

lr.fit(X_train_under, y_train_under)
y_pred_under = lr.predict(X_test)

cm_under = confusion_matrix(y_test, y_pred_under)
print('Confusion matrix (Undersampling):\n')
print(cm_under)
print('\nClassification report (Undersampling):\n')
print(classification_report(y_test, y_pred_under))

smote = SMOTE(random_state=42)
X_train_over, y_train_over = smote.fit_resample(X_train, y_train)

lr.fit(X_train_over, y_train_over)
y_pred_over = lr.predict(X_test)

accuracy_over = accuracy_score(y_test, y_pred_over)

cm_over = confusion_matrix(y_test, y_pred_over)
print('Confusion matrix (Oversampling):\n')
print(cm_over)
print('\nClassification report (Oversampling):\n')
print(classification_report(y_test, y_pred_over))

"""Apply KNN method to detect outlier. (Main)"""

import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

X = np.random.normal(size=(100, 2))

n_neighbors = 5

nbrs = NearestNeighbors(n_neighbors=n_neighbors+1, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
distances = distances[:,1:]
avg_distances = np.mean(distances, axis=1)

outliers_knn = np.where(avg_distances > np.mean(avg_distances) + 2*np.std(avg_distances))[0]

dbscan = DBSCAN(eps=0.3, min_samples=n_neighbors)
dbscan.fit(X)

outliers_dbscan = np.where(dbscan.labels_ == -1)[0]

print('KNN outliers:', outliers_knn)

print('DBSCAN outliers:', outliers_dbscan)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c='b', label='Data Points')
plt.scatter(X[outliers_knn, 0], X[outliers_knn, 1], c='r', label='KNN Outliers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Outlier Detection using KNN')
plt.legend()
plt.show()