def classifyDt(features_train, labels_train, features_test):
    ### your code goes here--should return a trained decision tree classifer
    from sklearn.tree import  DecisionTreeClassifier
    clf=DecisionTreeClassifier(min_samples_split=100)
    clf.fit(features_train, labels_train)
    return clf