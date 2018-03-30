# By default, only functions whose name that start with test are run.
# https://stackoverflow.com/questions/13626524/unit-test-not-running

import unittest
import sys
sys.path.append("../src")
#sys.path.append("../src/SampleTxtFiles")
from WordTagger import WordTagger

class Tester(unittest.TestCase):

    def test_verbose(self):
        tagger = WordTagger()
        self.assertEqual(tagger.verboseMode, False)
        tagger.verboseModeOn()
        self.assertEqual(tagger.verboseMode, True)

    def test_innitFile(self):
        tagger = WordTagger()
        tagger.innitFile("../src/SampleTxtFiles/poem_of_unicorn.txt")
        #print("Content of the afterReading:\n", tagger.afterReading)
        self.assertEqual(tagger.afterReading, open("../src/SampleTxtFiles/poem_of_unicorn.txt", "r").read())

    def test_addTriggerPattern(self):
        tagger = WordTagger()
        #Reference to Gundam Seed Astray
        tagger.addTriggerPattern("Red Frame")
        tagger.addTriggerPattern("Blue Frame")
        self.assertEqual(tagger.triggerPattern, ["Red Frame", "Blue Frame"])

    def test_tokenizeNeedsTagging(self):
        tagger = WordTagger()
        tagger.innitFile("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeNeedsTagging()
        self.assertEqual(tagger.tokens, ["sample", "sample", "sample"])

    def test_countFrequency(self):
        tagger = WordTagger()
        tagger.innitFile("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeNeedsTagging()
        tagger.countFrequency("sample")
        self.assertEqual(tagger.isCounter, 3)

    def test_matchPattern(self):
        tagger = WordTagger()
        tagger.innitFile("../src/SampleTxtFiles/sample_one.txt")
        tagger.tokenizeNeedsTagging()
        tagger.addTriggerPattern("sample")
        tagger.matchPattern()
        self.assertEqual(tagger.isCounter, 3)

if __name__ == "__main__":
    unittest.main()
