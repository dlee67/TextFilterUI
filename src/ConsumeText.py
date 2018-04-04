import sys
import os
from ProcessText import ProcessText

'''
    ConsumeText is an object which encapsulates the listOfProcessedText, and able to populate it with an
    ease.
'''
class ConsumeText(object):

    def __init__(self):
        self.listOfProcessedText = []

# The populateList will have to look for the pool of text files, and the triggerPatterns which
# needs to be passed in to the ProcessText object.
# Just for the reminder, if a user wants to populate listOfProcessedText with 10 objects,
# then this function must be called 10 times.
    def populateList(self, fileDirectory, triggerPatterns):
        fileBeingProcessed = ProcessText()
        fileBeingProcessed.fileToString(fileDirectory)
        fileBeingProcessed.setTriggerPattern(triggerPatterns)
        fileBeingProcessed.tokenizeTextFileContent()
        fileBeingProcessed.matchPattern()
        fileBeingProcessed.setTokenCount()
        fileBeingProcessed.finalize()
        self.listOfProcessedText.append(fileBeingProcessed)
