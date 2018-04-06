import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inputGenerator

from FeedText import FeedText
from scipy import sparse
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

#targetValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#			  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#inputValues = inputGenerator.generateInput(len(targetValues))

def plotValues(userInput):
	for counter in range(0, len(userInput)):
		plt.scatter(plotThis[counter][0], plotThis[counter][1])
	plt.xlabel("x-axis")
	plt.ylabel("y-axis")
	plt.show()

def plotRegression(inputValues, targetValues):
	svm = LinearSVC(C=1)
	svm.fit(inputValues, targetValues)
	w = svm.coef_[0]
	a = -w[0]/w[1]
	xx = np.linspace(0, 20)
	yy = a * xx - (svm.intercept_[0]) / w[1]
	for counter in range(0, len(inputValues)):
		plt.scatter(inputValues[counter][0], inputValues[counter][1])
	plt.plot(xx, yy)
	plt.show()

def predictUserInput(userInput, input, target):
	knn = Kn(n_neighbors=1)
	knn.fit(input, target)
	result = knn.predict([predictThis])
	print("predict() returned: ", result)

plotValues(inputValues)
plotRegression(inputValues, targetValues)

startProg([0, 9], inputValues, targetValues)
startProg([4, 7], inputValues, targetValues)
startProg([11, 19], inputValues, targetValues)
startProg([12, 17], inputValues, targetValues)
startProg([0, 20], inputValues, targetValues)
