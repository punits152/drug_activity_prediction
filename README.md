# Problem Statement
Drugs are typically small organic molecules that achieve their desired activity by binding to a target site on a receptor. The first step in the discovery of a new drug is usually to identify and isolate the receptor to which it should bind, followed by testing many small molecules for their ability to bind to the target site. This leaves researchers with the task of determining what separates the active (binding) compounds from the inactive (non-binding) ones. Such a determination can then be used in the design of new compounds that not only bind, but also have all the other properties required for a drug (solubility, oral absorption, lack of side effects, appropriate duration of action, toxicity, etc.). 

The goal is to to develop predictive models that can determine given a particular compound whether it is active (1) or not (0).
A molecule can be represented by 100000 binary features which represent their topological shapes and other characteristics important for binding.

# Dataset
## Caveats: 
 The dataset has an imbalanced distribution i.e., within the training set there are only 78 actives (+1) and 722 inactives (0). No information is provided for the test set regarding the distribution.
## Description
Input matrix has shape of 800*100000 and the test data have a matrix of shpe 350*100000.

# Application Architecture and Module Division
![](/info/architecture.jpeg "Architecture")


# Code Explanation

## Data ingestion

## Data Preprocessing

## Model Selection

## Model Tuning 

## Prediction 

## Logging Framework

## Deployment
