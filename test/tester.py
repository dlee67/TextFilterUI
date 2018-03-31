# By default, only functions whose name that start with test are run.
# https://stackoverflow.com/questions/13626524/unit-test-not-running

import unittest
import sys
sys.path.append("../src")
#sys.path.append("../src/SampleTxtFiles")
import os
from ProcessText import ProcessText
from unittest import TestCase

class Tester(unittest.TestCase):

    def test_verbose(self):
        tagger = ProcessText()
        self.assertEqual(tagger.verboseMode, False)
        tagger.verboseModeOn()
        self.assertEqual(tagger.verboseMode, True)

    def test_fileToString(self):
        tagger = ProcessText()
        tagger.fileToString("../src/SampleTxtFiles/poem_of_unicorn.txt")
        #print("Content of the textFileContent:\n", tagger.textFileContent)
        self.assertEqual(tagger.textFileContent, open("../src/SampleTxtFiles/poem_of_unicorn.txt", "r").read())

    def test_addTriggerPattern(self):
        tagger = ProcessText()
        #Reference to Gundam Seed Astray
        tagger.addTriggerPattern("Red Frame")
        tagger.addTriggerPattern("Blue Frame")
        self.assertEqual(tagger.triggerPattern, ["Red Frame", "Blue Frame"])

    def test_tokenizeTextFileContent(self):
        tagger = ProcessText()
        tagger.fileToString("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeTextFileContent()
        self.assertEqual(tagger.tokens, ["sample", "sample", "sample"])

    def test_countFrequency(self):
        tagger = ProcessText()
        tagger.fileToString("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeTextFileContent()
        tagger.countFrequency("sample")
        self.assertEqual(tagger.patternMatchCount, 3)

    def test_matchPattern(self):
        tagger = ProcessText()
        tagger.fileToString("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeTextFileContent()
        tagger.addTriggerPattern("sample")
        tagger.matchPattern()
        self.assertEqual(tagger.patternMatchCount, 3)

    def test_changeMatchCountThreshold(self):
        tagger = ProcessText()
        self.assertEqual(tagger.matchCountThreshold, 5)
        # Trying to supply the changeMatchCountThreshold() with value from the stdin,
        # don't know how to, yet.
        # 03/30/18 Gave up on having the python generate the mock stdin for now.
        tagger.changeMatchCountThreshold(3)
        self.assertEqual(tagger.matchCountThreshold, 3)
        tagger.changeMatchCountThreshold(int(-3))
        self.assertEqual(tagger.matchCountThreshold, 5)

    def test_finalize(self):
        tagger = ProcessText()
        tagger.finalize()
        self.assertEqual(tagger.isCategory, False)
        tagger.patternMatchCount = 7
        tagger.tokenCount = 30
        tagger.finalize()
        self.assertEqual(tagger.isCategory, True)

    def test_setTokenCount(self):
        tagger = ProcessText()
        tagger.fileToString("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeTextFileContent()
        tagger.setTokenCount()
        self.assertEqual(tagger.tokenCount, 3)

    def test_setTokenCountThreshold(self):
        tagger = ProcessText()
        tagger.fileToString("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeTextFileContent()
        self.assertEqual(tagger.tokenCountThreshold, 25)
        tagger.setTokenCountThreshold(5)
        self.assertEqual(tagger.tokenCountThreshold, 5)

if __name__ == "__main__":
    unittest.main()
