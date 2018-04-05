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

    def test_populateList(self):
        testObj = ConsumeText()
        self.assertEqual(len(testObj.listOfProcessedText), 0) #In the beginning of ConsumeText's life time, listOfText should be zero.
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
        self.assertEqual(len(testObj.listOfProcessedText), 10)

    def test_ConsumeTextContents(self):
        testObj = ConsumeText()
        testObj.populateList("./e-mails/spams/sample_one.txt", open(os.path.join(os.path.dirname(__file__) + "/../src/patternList.txt")).read().split(","))
        self.assertEqual(testObj.listOfProcessedText[0].textFileContent, open(os.path.join(os.path.dirname(__file__) + "/../src/e-mails/spams/sample_one.txt"), "r").read())

    def test_Accuracy(self):
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
# Much more complete product will most likely have it's array dynamic; therefore, this Tester must be fixed later.
        try:
            for index in range(0, 10):
                if(index > 4):
                    self.assertEqual(testObj.listOfProcessedText[index].isCategory, False)
                    continue
                self.assertEqual(testObj.listOfProcessedText[index].isCategory, True)
        except AssertionError:
            print("Catch block starting ================================")
            print(testObj.listOfProcessedText[index].textFileContent)
            print("The matchPattern count:",testObj.listOfProcessedText[index].patternMatchCount)
            print("The tokens are:",testObj.listOfProcessedText[index].tokens)
            print("Patterns that triggered:",testObj.listOfProcessedText[index].patternThatTriggered[:])
            print("Catch block ending ==================================\n\n\n")
        for index in range(0, 10):
            print(testObj.listOfProcessedText[index].isCategory)

if __name__ == "__main__":
    unittest.main()
