#!/usr/bin/python
import sys
from time import time
from sklearn import svm
sys.path.append("../tools/")
from email_preprocess import preprocess

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""
    



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# decrease training set size
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf = svm.SVC(C=1.0, kernel='linear')
clf.fit(features_train, labels_train)
t1 = time()
print("prediction accuracy: {}".format(clf.score(features_test, labels_test)))
t2 = time()
print("training time: {0}s ({1} data points), prediction time: {2}s ({3} data points)".format(round(t2-t0, 3), len(features_train), round(t2-t1, 3), len(features_test)))
#########################################################


