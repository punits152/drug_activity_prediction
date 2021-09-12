import numpy as np
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


def get_reduced(X,Y,logger_obj,log_file_obj):
    """
    This function will provide the reduced data in train and test format
    """

    # I will decide between PCA or SparsePCA for reference see notebook
    num_compo = 500
    pca = PCA(n_components=num_compo,random_state=1234,svd_solver="auto")
    X_reduced = pca.fit_transform(X)
    explained_variance = np.sum(pca.explained_variance_ratio_)
    logger_obj.log(log_file_obj,f"Successfully reduced dimensions to {num_compo} with total {explained_variance}% of variance explained")

    # Now I will create the train and test data

    X_train, X_test, y_train, y_test = train_test_split(X_reduced,Y)

    logger_obj.log(log_file_obj,"Train and Test data created")

    return (X_train,X_test,y_train,y_test)

#def decision_tree_classifier(X_train,X_test,y_train,y_test):
    # will use gridsearchCV to find the best classifier




