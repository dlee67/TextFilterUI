import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from FeedText import FeedText
from scipy import sparse
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

class MLAlg(object):

    def __init__(self):
# For the K-neighbors algrithm to classify certain data points.
        self.targetValues = None
# Input values are composed of x and y values, where x value represents patternMatchCount,
# and the y value represents token counts.
        self.inputValues = None

    def setTargetValues(self, userInput):
        self.targetValues = userInput

    def setInputValues(self, userInput):
        self.inputValues = userInput

    def plotValues(self):
        for counter in range(0, len(self.inputValues)):
            plt.scatter(self.inputValues[counter][0], self.inputValues[counter][1])
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.show()

    def plotRegression(self):
        svm = LinearSVC(C=1)
        svm.fit(self.inputValues, self.targetValues)
        w = svm.coef_[0]
        a = -w[0]/w[1]
        xx = np.linspace(0, 20)
        yy = a * xx - (svm.intercept_[0]) / w[1]
        for counter in range(0, len(self.inputValues)):
            plt.scatter(self.inputValues[counter][0], self.inputValues[counter][1])
        plt.plot(xx, yy)
        plt.show()

# userInput parameter in this function represents the ProcessedText object, which needs to be
# innitialized before the usage of this function.
    def predictUserInput(self, userInput):
        knn = Kn(n_neighbors=1)
        knn.fit(self.inputValues, self.targetValues)
        result = knn.predict([userInput.patternMatchCount, userInput.tokenCount])
        print("predict() returned: ", result)
