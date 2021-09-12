# Problem Statement
Drugs are typically small organic molecules that achieve their desired activity by binding to a target site on a receptor. The first step in the discovery of a new drug is usually to identify and isolate the receptor to which it should bind, followed by testing many small molecules for their ability to bind to the target site. This leaves researchers with the task of determining what separates the active (binding) compounds from the inactive (non-binding) ones. Such a determination can then be used in the design of new compounds that not only bind, but also have all the other properties required for a drug (solubility, oral absorption, lack of side effects, appropriate duration of action, toxicity, etc.). 

The goal is to to **develop predictive models that can determine given a particular compound whether it is active (1) or not (0)**.
A molecule can be represented by 100000 **binary** features which represent their topological shapes and other characteristics important for binding.

# Dataset
## Caveats: 
 The dataset has an imbalanced distribution i.e., within the training set there are only 78 actives (+1) and 722 inactives (0). No information is provided for the test set regarding the distribution.
## Description
Input matrix has shape of 800-100000 and the test data have a matrix of shpe 350-100000.
Data is a **sparse matrix** of 100000 binary attributes so for eaach observation only the indices of the non zero column are provided.

# Application Architecture and Module Division
![](/info/architecture.jpeg "Architecture")


# Code Explanation

## Data ingestion
The data was not in a conventional csv format but the data was in a tax file. Since our data have 100000 columns and all are of binary nature so the indices of the columns for each observation, that are non zero are provided.
To tackle this problem the data was read from a classical text file and was converted to data frame using Data_Getter class.
I have not converted this data frame to csv due to its size.

A validation data with labels is also given for 350 observations. I will use crossvalidation for hyperparameter tuning and will use this validation set as the test data. I will use test data for predictions. You are free to suggest amendments.


## Model Selection
There are two challanges here in modelling the classifier: 
1. Number of features is very high 
2. Data is imbalanced as there are only 78 active cases and 722 observations are inactive, therefore F1 score is preferred over accuracy score for assessing the predictions.

The approaches used for dimensionality reduction are:
* Principle Component Analysis
* **Sparse PCA** (With L1 penalty tuning)
For PCA I will code in notebook, in directory model_eda, for the number of components taken and the vriance described by them.

ML models tried for classification are:
  1. KNN
  2. Decision Tree
  3. Adaboost
  4. Random Forest
  5. SVM
  6. Logistic Regression

Most of the algorithms, being non-parametric, won't require **SMOTE(Synthetic Minority Oversampling Technique)** or any such oversampling technique. But I will use SMOTE in some cases.


## Model Tuning 

## Prediction 

## Logging Framework

## Deployment
