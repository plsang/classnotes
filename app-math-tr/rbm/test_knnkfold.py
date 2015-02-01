import cPickle, numpy as np, gzip
from sklearn import neighbors
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

X = np.loadtxt('binarydigits.txt')
Y = np.ravel(np.loadtxt('bindigitlabels.txt'))

from sklearn.cross_validation import KFold
scores = []
cv = KFold(n=len(X),n_folds=3)
for train, test in cv:
    X_train, Y_train = X[train], Y[train]
    X_test, Y_test = X[test], Y[test]
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, Y_train)
    scores.append(clf.score(X_test, Y_test))
    
print np.mean(scores)
            
# 97    
