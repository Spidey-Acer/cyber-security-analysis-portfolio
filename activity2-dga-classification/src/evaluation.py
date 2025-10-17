"""Evaluation utilities"""
from sklearn.metrics import classification_report

def evaluate_model(clf, X_test, y_test):
    preds = clf.predict(X_test)
    return classification_report(y_test, preds)
