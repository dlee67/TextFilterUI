import unittest
import sys
sys.path.append("../src")
import os
#os.chdir("../src/e-mails")
from ConsumeText import ConsumeText
from ProcessText import ProcessText
from FeedText import FeedText
from unittest import TestCase
from unittest.mock import patch
from unittest import TestCase

class Test(unittest.TestCase):

    def test_innitialization(self):
        feedTextObj = FeedText()
        self.assertEqual(feedTextObj.taggerPattern, open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        self.assertEqual(feedTextObj.consumedTexts, None)

    def test_setDirectory(self):
        feedTextObj = FeedText()

    def consumeTextFiles(self):
        pass
