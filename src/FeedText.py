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
        self.taggerPattern = open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(",")

    def setDirectory(self, userInput):
        self.directory = userInput

# The function takes in the user specified directory.
# https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
# Going to use the technique specified in the above link.
# Let's obligate the user to call setDirectory, before letting use the consumeTextFiles
    def consumeTextFiles(self, userInput):
        consumeTextObj = ConsumeText()
        # Fetch all the file names within the user specified directory.
        listOfFiles = os.listdir(Path(userInput))
# For all the content inside the specified directory, all the .txt files will be "parsed" into the consumeTextObj's
# listOfProcessedText.
        for fileName in listOfFiles:
            if(fileName.contains(".txt")):
                consumeTextObj.populateList(userInput + "/" + fileName, self.taggerPattern)

#    def toTargetValues(self):
