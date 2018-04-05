import nltk
import os
import sys
sys.path.append("../src")
from ConsumeText import ConsumeText
from pathlib import Path

'''
    I will likely have to add a functionality which consumes all the text files in some sort of "pool."
'''

class FeedText(object):

    def __init__(self):
        self.consumedTexts = None
        self.directory = None
        self.listOfFiles = None
        self.taggerPattern = open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(",")

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
    def consumeTextFiles(self, userInput):
        self.consumedTexts = ConsumeText()
# Uses the list of string tokens as the reference, to populateList
        for fileName in self.listOfFiles:
            if(fileName.contains(".txt")):
                consumedTexts.populateList(userInput + "/" + fileName, self.taggerPattern)
