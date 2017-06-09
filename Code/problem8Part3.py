"""
 EE232E Project 2 Problem 8 Part 3
 Name: Weikun Han, Duzhi Chen
 Date: 6/4/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
  - http://scikit-learn.org/stable/
 Description:
  - Train a ordinary least squares Linear Regression model to predict movie rating
"""

from __future__ import print_function
from sklearn import datasets, linear_model
from sklearn.metrics import r2_score

# Print information
print(__doc__)
print()

y_true = [6.7, 7.4, 6.4]



movie={}
movie_file=open('movie_feature.txt','r')


# Load the diabetes dataset

movie_dict = {}
movie_id = 1
for line in movie_file.readlines():
    tokens = line.split("\t")
    diabetes = [token[0], token[1], token[2]. token[3]]


movie_file.close()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

y_pred = regr.predict(X_test)





# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Construct ordinary least squares Linear Regression model successfully!")
print("The predict rating of Batman vs Superman: Dawn of Justice (2016): %.1f" % y_pred[0])
print("The predict rating of Mission: Impossible - Rogue Nation (2015): %.1f" % y_pred[1])
print("The predict rating of Minions (2015): %.1f" % y_pred[2])
print("The score of the R2 is: %f" % r2_score(y_true, y_pred) )
print("--------------------------------------------------------------------")
print()
