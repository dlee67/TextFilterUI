import nltk
import os
import sys
sys.path.append("../src")
from ConsumeText import ConsumeText
from pathlib import Path

'''
	On an abstarct sense, this class inntializes the ConsumeText object with meaningful data,
	and innitializes itself with the meaninful data to be fed to MLAlg.py; so, it could be processed
	in the K-Neighbors alogrithm.
'''

class FeedText(object):

    def __init__(self):
        self.consumedTexts = ConsumeText()
        self.directory = None
        self.listOfFiles = None
        self.taggerPattern = open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(",")
        self.targetValues = []
        self.inputValues = None

# It might be a good idea to have the user always pass in the relative path.
    def setDirectory(self, userInput):
        self.directory = userInput

# Fetch all the file names in the user specified directory.
    def setListOfFiles(self):
        self.listOfFiles = os.listdir(Path(self.directory))

# The function takes in the user specified directory.
# https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
# Going to use the technique specified in the above link.
# Let's obligate the user to call setDirectory, and setListOfFiles, before letting use the consumeTextFiles
# For all the content inside the specified directory, all the .txt files will be "parsed" into the consumeTextObj's
# listOfProcessedText.
    def consumeTextFiles(self):
# Uses the list of string tokens as the reference, to populateList
        for fileName in self.listOfFiles:
            if((fileName.find(".txt") >= 0)):
                self.consumedTexts.populateList(self.directory + "/" + fileName, self.taggerPattern)

# Generate the target values for the machine learning algorithm I am about to feed this data to.
    def generateTargetValues(self):
        for obj in self.consumedTexts.listOfProcessedText:
            if (obj.isCategory == True):
                self.targetValues.append(0)
            elif (obj.isCategory == False):
                self.targetValues.append(1)
        self.targetValues.sort()

# The function needs to assign 2-dimensional array to
# input values.
    def generateInputValues(self):
        self.inputValues = []
        for obj in self.consumedTexts.listOfProcessedText:
            newElement = [obj.patternMatchCount, obj.tokenCount]
            self.inputValues.append(newElement)
