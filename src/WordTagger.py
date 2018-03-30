# Turns out, read() doesn't return anything.
# https://stackoverflow.com/questions/3211031/python-file-read
import nltk

class WordTagger(object):
# The isCounter will be used to assign the boolean value of is category, after certain limit has passed.
# needsTagging is the fresh text file, that needs to be tokenized.
# afterReading is the text file in the form of string data type.
# tokens are the string tokens fetched from the needsTagging.
# triggerPattern is user specified string tokens, which will increment the isCounter.
# verboseMode, when true, will obligate the WordTagger.py to verbosely explain everything that is going on.
# isCategory will have to be assigned with a True value, if the isCounter exceeds the specified limit.
    def __init__(self):
        self.isCounter = 0
        self.needsTagging = None
        self.afterReading = None
        self.tokens = None
        self.triggerPattern =[]
        self.verboseMode = False
        self.isCategory = False
        print("WordTagger has been innitialized.")

# As the name suggests
    def printAfterReading(self):
        print("Consumed content\n:", self.afterReading, "\n")

# As the name suggests
    def printTriggerPattern(self):
        print("The patterns for incrementing the counter is: ", self.triggerPattern[:])

# As the name suggests
    def printCounter(self):
        print("Currently, the amount of counter is: ", self.isCounter)

#   By comparing the tokens to the user specified patterns, increment the isCounter.
    def matchPattern(self):
        freqDist = nltk.FreqDist(self.tokens)
        for pattern in self.triggerPattern:
            if(verboseMode == True):
                print("Current pattern: ", pattern)
                print("Current frequency of the pattern: ", freqDist[pattern])
            self.isCounter = self.isCounter + freqDist[pattern]

#The method below was created with regex pattern in mind.
# As the name suggests
    def addTriggerPattern(self, userInput):
        if(self.verboseMode):
            print("In the addTriggerPattern block.")
        self.triggerPattern.append(str(userInput))
        if(self.verboseMode):
            print("The list of trigger pattern is: ", triggerPattern[:])

# As the name suggests
    def verboseModeOn(self):
        self.verboseMode = True

# As the name suggests
    def innitFile(self, fileName):
        if(self.verboseMode):
            print("In the block of innitFile.")
        self.needsTagging = open(fileName, "r")
        self.afterReading = self.needsTagging.read()

# As the name suggests
    def tokenizeNeedsTagging(self):
        if(self.verboseMode):
            print("In the block for tokenizeNeedsTagging.")
        self.tokens = nltk.word_tokenize(self.afterReading)

# Increment the isCounter separate from the matchPattern method, and string token specified by the user.
# In this case, findThis argument will be used for comparison, and the isCounter will be incremented
# according to that.
    def countFrequency(self, findThis, limit=3):
        fDistObj = nltk.FreqDist(self.tokens)
        if(self.verboseMode):
            print("Consumed:", fDistObj.keys())
        amtOfOccur = fDistObj[findThis]
        #I am guessing the frequency distribution cannot consume anything aside from
        #tokenized string.
        print("The word", findThis, "has occured this much:", amtOfOccur)
        if(limit > 3):
            if(input("The frequency of the specified token has occured for more than 3 times, increase the counter? Type n for no") == "n"):
                return;
            isCounter = isCounter + 1

# As the name suggests
    def toString(self):
        print("The needTagging is: ", self.needTagging.read(),
                "\n as a type of: ", type(self.needTagging.read()))
        print("The tokens are: ",  self.tokens,
            "\n as a type of: ", type(self.tokens))
        print("After reading: ", self.afterReading)

# As the name suggests
    def listFunctions(self):
        print("verboseModeOn <- Each functions prints out the results.\n",
                "innitFile <- Consumes the text file, and prepares it to be tokenized.\n",
                "tokenizeNeedsTagging <- Tokenizes the consumed text file.\n",
                "countFrequency <- Counts the frequency of a certain string token.\n",
                "toString <- prints out all the contents within the fields of WordTagger object, with it's data type.")
