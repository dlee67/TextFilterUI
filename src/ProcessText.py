# Turns out, read() doesn't return anything.
# https://stackoverflow.com/questions/3211031/python-file-read
import nltk
import os
import sys
#sys.path.append("./e-mails")

class ProcessText(object):
# patternMatchCount is increased each time when the userSpecified patterns are matched in the text being processed.
# tokenCount is set to the amount of token existing.
# tokenCountThreshold will be used in the finalize() to determine the boolean value of the isCategory
# innitialTextFile is the fresh text file, that needs to be tokenized.
# textFileContent is the text file in the form of string data type.
# tokens are the string tokens fetched from the innitialTextFile.
# triggerPattern is user specified string tokens, which will increment the patternMatchCount.
# verboseMode, when true, will obligate the ProcessText.py to verbosely explain everything that is going on.
# isCategory will have to be assigned with a True value, if the patternMatchCount exceeds the specified limit.
    def __init__(self):
        self.patternMatchCount = 0
        self.matchCountThreshold = 5
        self.tokenCount = 0
        self.tokenCountThreshold = 25
        self.isCategory = False

        self.innitialTextFile = None
        self.textFileContent = None
        self.tokens = None
        self.triggerPattern =[]
        self.verboseMode = False
        print("ProcessText has been innitialized.")

# Prints out the content inside the textFileContent
    def printTextFileContent(self):
        print("Consumed content\n:", self.textFileContent, "\n")

# Prints out the content inside the triggerPattern
    def printTriggerPattern(self):
        print("The patterns for incrementing the counter is: ", self.triggerPattern[:])

# Prints out the content inside the patternMatchCount
    def printPatternMatchCount(self):
        print("Currently, the amount of counter is: ", self.patternMatchCount)

# By comparing the tokens to the user specified patterns, increment the patternMatchCount.
    def matchPattern(self):
        freqDist = nltk.FreqDist(self.tokens)
        for pattern in self.triggerPattern:
            if(self.verboseMode == True):
                print("Current pattern: ", pattern)
                print("Current frequency of the pattern: ", freqDist[pattern])
            self.patternMatchCount = self.patternMatchCount + freqDist[pattern]

# Enables the user to append a pattern to the triggerPattern list, which will be used to increment
# the patternMatchCount, each time when the user specified pattern is found.
    def addTriggerPattern(self, userInput):
        if(self.verboseMode):
            print("In the addTriggerPattern block.")
        self.triggerPattern.append(str(userInput))
        if(self.verboseMode):
            print("The list of trigger pattern is: ", triggerPattern[:])

# The verbose mode will enable the user to
    def verboseModeOn(self):
        self.verboseMode = True

# Fetches the method of the text file content, and assigns to textFileContent
    def fileToString(self, fileName):
        if(self.verboseMode):
            print("In the block of fileToString.")
        fileName = os.path.join(os.path.dirname(__file__), fileName)
        self.innitialTextFile = open(fileName, "r")
        self.textFileContent = self.innitialTextFile.read()
        self.innitialTextFile.close()

# As the name suggests
    def tokenizeTextFileContent(self):
        if(self.verboseMode):
            print("In the block for tokenizeTextFileContent.")
        self.tokens = nltk.word_tokenize(self.textFileContent)

# Increment the patternMatchCount separate from the matchPattern method, and string token specified by the user.
# In this case, findThis argument will be used for comparison, and the patternMatchCount will be incremented
# according to that.
# Each time when the specified pattern is found, increase the patternMatchCount.
    def countFrequency(self, findThis, limit=3):
        fDistObj = nltk.FreqDist(self.tokens)
        if(self.verboseMode):
            print("Consumed:", fDistObj.keys())
        amtOfPatternOccurred = fDistObj[findThis]
        #I am guessing the frequency distribution cannot consume anything aside from
        #tokenized string.
        print("The word", findThis, "has occured this much:", amtOfPatternOccurred)
        self.patternMatchCount = self.patternMatchCount + amtOfPatternOccurred

    def setTriggerPattern(self, userInput):
        self.triggerPattern = userInput

    def setTokenCount(self):
        self.tokenCount = len(self.tokens)

    def setTokenCountThreshold(self, userInput):
        if(int(userInput) <= 0):
            print("Input must be bigger than 0, setting the tokenCountThreshold to default (which is 25).")
            self.tokenCountThreshold = 25
            return
        self.tokenCountThreshold = int(userInput)

# As the name suggests
    def toString(self):
        print("The needTagging is: ", self.needTagging.read(),
                "\n as a type of: ", type(self.needTagging.read()))
        print("The tokens are: ",  self.tokens,
            "\n as a type of: ", type(self.tokens))
        print("After reading: ", self.textFileContent)

# As the name suggests
    def listFunctions(self):
        print("verboseModeOn <- Each functions prints out the results.\n",
                "fileToString <- Consumes the text file, and prepares it to be tokenized.\n",
                "tokenizeTextFileContent <- Tokenizes the consumed text file.\n",
                "countFrequency <- Counts the frequency of a certain string token.\n",
                "toString <- prints out all the contents within the fields of ProcessText object, with it's data type.")

    def changeMatchCountThreshold(self, userInput):
        if(self.verboseMode == True):
            print("The current matchCountThreshold is:", self.matchCountThreshold)
        if((userInput > 0) == False):
            print("Invalid input, changing the matchCountThreshold to default value 5.")
            self.matchCountThreshold = 5
            return
        self.matchCountThreshold = userInput

    def finalize(self):
        print("finalized called.\n")
        print("Token count now:", self.tokenCount, "\n")
        print("Pattern match count:", self.patternMatchCount, "\n")
        if((self.matchCountThreshold <= self.patternMatchCount) and (self.tokenCountThreshold <= self.tokenCount)):
            self.isCategory = True
            return
        return
