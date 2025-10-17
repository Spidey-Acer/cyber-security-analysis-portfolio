"""Model training utilities"""
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X, y)
    return clf
