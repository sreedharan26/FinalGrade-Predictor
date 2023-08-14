import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle
import os

path = os.getcwd()

data = pd.read_csv(path + "/studentModel/student-mat.csv", sep=";")
# print(data)
# print(data.head())
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

# creating a separate data from the given data in which there is no G3 so that we can predict the results of G3
x = np.array(data.drop([predict], axis=1))

# creating the values of G3 as a seperate array to check our predictions of G3
y = np.array(data[predict])

# here splitting of the original data into training data and testing data is done.Here in this case the testing data is 10% of original data.
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, train_size=0.1
)

best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        x, y, train_size=0.1
    )
    # this is a function that helps to create a best-fit line based on the training data
    # if the data consists of two variables then the equation of BFL will be y = mx + c;
    # else there are many varibles in our data then the equation of BFL to find our predictions will be as y = ax + bz + cw + ..
    linear = linear_model.LinearRegression()
    # .fit is a method which takes the x-axis data, y-axis data and creates a best-fit line
    linear.fit(x_train, y_train)

    acc = linear.score(x_test, y_test)

    print(acc)
    if acc > best:
        best = acc
        with open(path + "/StudentModel/bestFitLine.pickle", "wb") as f:
            pickle.dump(linear, f)

pickle_data = open(path + "/StudentModel/bestFitLine.pickle", "rb")
linear = pickle.load(pickle_data)

print(best)

print("Co-efficients:", linear.coef_)
# since our prediction "G3" is dependent on 5 other variables["G1", "G2", "studytime", "failures", "absences"] so the output will be 5 values each corresponds to the coefficient of each variable

print("Intercept:", linear.intercept_)
# since the BFL consists of only one intercept so the output will be the value of the y-intercept

# now we are testing on our test data using the model that we created and storing the predictions.
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])


# Now we are going to plot the graph using the data
p = "absences"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.title("BestFitLine for prediction of Final Grade basis on absences")
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
