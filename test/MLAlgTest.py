import unittest
import sys
sys.path.append("../src")
import os
#os.chdir("../src/e-mails")
from ConsumeText import ConsumeText
from ProcessText import ProcessText
from FeedText import FeedText
from MLAlg import MLAlg
from unittest import TestCase
from unittest.mock import patch
from unittest import TestCase

class Test(unittest.TestCase):

    def test_setTargetValues(self):
        kAlg = MLAlg()
        feedText = FeedText()
        processedTextStrings = []

        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/spams")
        feedText.setListOfFiles() # Innitialize the list of file names.
        feedText.consumeTextFiles() # In the specified directory, with the set of file names, populate the list in ConsumeText object.
        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/non-spams")
        feedText.setListOfFiles()
        feedText.consumeTextFiles()
        feedText.generateTargetValues()
        kAlg.setTargetValues(feedText.targetValues)
        self.assertEqual(kAlg.targetValues, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    def test_createUserInput(self):
        kAlg = MLAlg()
        feedText = FeedText()
        processedTextStrings = []
        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/spams")
        feedText.setListOfFiles() # Innitialize the list of file names.
        feedText.consumeTextFiles() # In the specified directory, with the set of file names, populate the list in ConsumeText object.
        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/non-spams")
        feedText.setListOfFiles()
        feedText.consumeTextFiles()
        feedText.generateInputValues()
        feedText.generateTargetValues()

        kAlg.setTargetValues(feedText.targetValues)
        kAlg.setInputValues(feedText.inputValues)
        kAlg.setTriggerPattern(feedText.taggerPattern)

        self.assertEqual(kAlg.createUserInputAndPredict("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/TestInput/sample_one.txt"), [1])
