import nltk
import os
import sys
from ConsumeText import ConsumeText

'''
    I will likely have to add a functionality which consumes all the text files in some sort of "pool."
'''

class FeedText(object):

    consumedTexts = None

    def toTargetValues(self):
