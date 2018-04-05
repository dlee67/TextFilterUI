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
        feedTextObj.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI")
        self.assertEqual(feedTextObj.directory, "/home/bob/Desktop/WorkSpace/TextFilterUI")

    def test_setListOfFile(self):
        feedText = FeedText()
        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/SampleTxtFiles")
        feedText.setListOfFiles()
        self.assertEqual("poem_of_unicorn.txt" in feedText.listOfFiles, True)
        self.assertEqual("sample_one.txt" in feedText.listOfFiles, True)
        self.assertEqual("sample_two.txt" in feedText.listOfFiles, True)

# So, each elements in the populated list must have the exact same content as the
# text files.
# Now that I think about it, I need to setDirectory twice, according to my design.
    def test_consumeTextFiles(self):
        feedText = FeedText()
        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/spams")
        feedText.setListOfFiles()
        feedText.consumeTextFiles()
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[0].read, open("../src/e-mails/spams/sample_one.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[1].read, open("../src/e-mails/spams/sample_two.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[2].read, open("../src/e-mails/spams/sample_three.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[3].read, open("../src/e-mails/spams/sample_four.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[4].read, open("../src/e-mails/spams/sample_five.txt").read)
        feedText.setDirectory("/home/bob/Desktop/WorkSpace/TextFilterUI/src/e-mails/non-spams")
        feedText.setListOfFiles()
        feedText.consumeTextFiles()
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[5].read, open("../src/e-mails/non-spams/sample_one.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[6].read, open("../src/e-mails/non-spams/sample_two.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[7].read, open("../src/e-mails/non-spams/sample_three.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[8].read, open("../src/e-mails/non-spams/sample_four.txt").read)
        self.assertEqaul(feedText.consumedTexts.listOfProcessedText[9].read, open("../src/e-mails/non-spams/sample_five.txt").read)
