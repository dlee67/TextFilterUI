import unittest
import sys
sys.path.append("../src")
import os
from ConsumeText import ConsumeText
from ProcessText import ProcessText
from unittest import TestCase
from unittest.mock import patch
from unittest import TestCase

class Tester(unittest.TestCase):

    def test_populateList(self):
        testObj = ConsumeText()
        self.assertEqual(len(testObj.listOfProcessedText), 0) #In the beginning of ConsumeText's life time, listOfText should be zero.
        testObj.populateList("./e-mails/spams/sample_one.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_two.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_three.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_four.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/spams/sample_five.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_one.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_two.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_three.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_four.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        testObj.populateList("./e-mails/non-spams/sample_five.txt", ["Dear", "Dong", "company"]) # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.
        self.assertEqual(len(testObj.listOfProcessedText), 10)

if __name__ == "__main__":
    unittest.main()
