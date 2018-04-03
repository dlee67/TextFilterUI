import sys
import os
from ProcessText import ProcessText

'''
    ConsumeTextTest needs to be able to have a list of ProcessText.py (where each of them has processed a text file, at least once).
'''

class ConsumeText(object):

    def __init__(self):
        self.listOfProcessedText = []

# The populateList will have to look for the pool of text files.
    def populateList(self, fileDirectory, triggerPatterns):
        fileBeingProcessed = ProcessText()
        fileBeingProcessed.fileToString(fileDirectory)
        fileBeingProcessed.addTriggerPattern(triggerPatterns)
        fileBeingProcessed.tokenizeTextFileContent()
        fileBeingProcessed.setTokenCount()
        fileBeingProcessed.finalize()
        self.listOfProcessedText.append(fileBeingProcessed)
