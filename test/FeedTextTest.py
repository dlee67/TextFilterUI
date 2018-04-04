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

class Test(unittest.TestCase):

# Must generate 1's and 0's from the false and true values.
    def test_toTargetValues(self):
        testObj = ConsumeText()
        testObj.populateList("./e-mails/spams/sample_one.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/spams/sample_two.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/spams/sample_three.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/spams/sample_four.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/spams/sample_five.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/non-spams/sample_one.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/non-spams/sample_two.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/non-spams/sample_three.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/non-spams/sample_four.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        testObj.populateList("./e-mails/non-spams/sample_five.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        
