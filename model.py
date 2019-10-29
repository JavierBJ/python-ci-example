from sklearn import datasets
from sklearn.linear_model import LinearRegression


def evaluate_model():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    clf = LinearRegression()
    clf.fit(X, y)

    return clf.score(X, y)
