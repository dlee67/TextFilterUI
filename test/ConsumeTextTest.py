# If I comment out sys.path, the from ConsumeText doesn't work,
# and if I comment out os.chdir eveyrthing just breaks...
# then, I mind as well program things centered around sys.path.

import unittest
import sys
sys.path.append("../src")
import os
#os.chdir("../src/e-mails")
from ConsumeText import ConsumeText
from ProcessText import ProcessText
from unittest import TestCase
from unittest.mock import patch
from unittest import TestCase

class Tester(unittest.TestCase):

    def feedTextFiles():
        testObj = ConsumeText()
        testObj.populateList("./e-mails/spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_two.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_three.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_four.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_five.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_two.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_three.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_four.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_five.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.

    def test_populateList(self):
        testObj = ConsumeText()
        self.assertEqual(len(testObj.listOfProcessedText), 0) #In the beginning of ConsumeText's life time, listOfText should be zero.
        testObj.populateList("./e-mails/spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_two.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_three.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_four.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_five.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_two.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_three.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_four.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_five.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        self.assertEqual(len(testObj.listOfProcessedText), 10)

    def test_ConsumeTextContents(self):
        testObj = ConsumeText()
        testObj.populateList("./e-mails/spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        self.assertEqual(testObj.listOfProcessedText[0].textFileContent, open(os.path.join(os.path.dirname(__file__) + "/../src/e-mails/spams/sample_one.txt"), "r").read())

    def test_Accuracy(self):
        testObj = ConsumeText()
        testObj.populateList("./e-mails/spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_two.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_three.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_four.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_five.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_one.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_two.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_three.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_four.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_five.txt", ["Job", "Category", "At least", "Requirements", "Training", "computer skills", "communication skills", "Salary", "position"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
# Much more complete product will most likely have it's array dynamic; therefore, this Tester must be fixed later.
        testObj.displayList()
        for index in range(0, 9):
            if(index > 4):
                self.assertEqual(testObj.listOfProcessedText[index].isCategory, False)
                continue
            self.assertEqual(testObj.listOfProcessedText[index].isCategory, True)

if __name__ == "__main__":
    unittest.main()
