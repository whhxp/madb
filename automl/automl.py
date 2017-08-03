# created by whh(whhxp1028@gmail.com)
# install automl first, see http://automl.github.io/auto-sklearn/stable/installation.html
# NOTE: change the command "pip" to "pip3" if you install version 2 and version 3 python in one system.

# Apart from auto-sklearn, Auto-WEKA is an alternative for Auto-ML, see
# Auto-WEKA 2.0: Automatic model selection and hyperparameter optimization in WEKA
# http://www.cs.ubc.ca/labs/beta/Projects/autoweka/



import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics

X, y = sklearn.datasets.load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, random_state=1)
automl = autosklearn.classification.AutoSklearnClassifier()
automl.fit(X_train, y_train)
y_hat = automl.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))
