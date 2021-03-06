import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(kernel="linear",C=1)#kernel="linear")


#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


#### store your predictions in a list named pred







def submitAccuracy(pred, labels_test):
    from sklearn.metrics import accuracy_score
    acc = accuracy_score(pred, labels_test)
    return acc

prettyPicture(clf, labels_test, features_test)
print(submitAccuracy())