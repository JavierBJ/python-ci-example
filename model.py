import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression

iris = datasets.load_iris()
X = iris.data
y = iris.target

clf = LinearRegression()
clf.fit(X,y)

print(clf.score(X,y))
