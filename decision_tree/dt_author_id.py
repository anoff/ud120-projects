#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
acc = clf.score(features_test, labels_test)
t2 = time()
print("prediction accuracy: {}".format(acc))
print("training time: {0}s ({1} data points), prediction time: {2}s ({3} data points)".format(round(t2-t0, 3), len(features_train), round(t2-t1, 3), len(features_test)))
#########################################################


