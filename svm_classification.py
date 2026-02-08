# svm_classification.py
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

# Assume features from previous file
# features = ... 
# y = ...

clf = SVC(kernel='linear')
scores = cross_val_score(clf, features, y, cv=5)
print("Cross-validation accuracy:", scores.mean() * 100, "%")
