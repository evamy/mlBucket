import pandas as pd
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


def bagging(X, Y, X_test, Y_test):
    clf = BaggingClassifier()
    scores = cross_val_score(clf, X, Y, cv=8, scoring='accuracy')
    return scores.mean()
