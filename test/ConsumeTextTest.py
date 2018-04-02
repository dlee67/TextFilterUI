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
        self.assertEqual(testObj.listOfText, 0) #In the beginning of ConsumeText's life time, listOfText should be zero.
        testObj.populateList() # Where ConsumeText will have list of ProcessText objects, waitingto be deciphered in the ML algorithm.

if __name__ == "__main__":
    unittest.main()
