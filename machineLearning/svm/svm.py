

import numpy as np
from sklearn                        import metrics, svm
from sklearn.linear_model           import LinearRegression
from sklearn.linear_model           import LogisticRegression
from sklearn.tree                   import DecisionTreeClassifier
from sklearn.neighbors              import KNeighborsClassifier
from sklearn.discriminant_analysis  import LinearDiscriminantAnalysis
from sklearn.naive_bayes            import GaussianNB
from sklearn.svm                    import SVC

trainingData    = np.array([ [2.3, 4.3, 2.5],  [1.3, 5.2, 5.2],  [3.3, 2.9, 0.8],  [3.1, 4.3, 4.0]  ]).astype('int64')
trainingScores  = np.array( [3.4, 7.5, 4.5, 1.6] ).astype('int64')
predictionData  = np.array([ [2.5, 2.4, 2.7],  [2.7, 3.2, 1.2] ]).astype('int64')

clf = LinearRegression()
clf.fit(trainingData, trainingScores)
print("LinearRegression")
print(clf.predict(predictionData))

clf = svm.SVR()
clf.fit(trainingData, trainingScores)
print("SVR")
print(clf.predict(predictionData))

clf = LogisticRegression()
clf.fit(trainingData, trainingScores)
print("LogisticRegression")
print(clf.predict(predictionData))

clf = DecisionTreeClassifier()
clf.fit(trainingData, trainingScores)
print("DecisionTreeClassifier")
print(clf.predict(predictionData))

# clf = KNeighborsClassifier()
# clf.fit(trainingData, trainingScores)
# print("KNeighborsClassifier")
# print(clf.predict(predictionData))
#
# clf = LinearDiscriminantAnalysis()
# clf.fit(trainingData, trainingScores)
# print("LinearDiscriminantAnalysis")
# print(clf.predict(predictionData))

clf = GaussianNB()
clf.fit(trainingData, trainingScores)
print("GaussianNB")
print(clf.predict(predictionData))

clf = SVC()
clf.fit(trainingData, trainingScores)
print("SVC")
print(clf.predict(predictionData))

