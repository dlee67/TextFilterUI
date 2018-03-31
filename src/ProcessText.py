# Turns out, read() doesn't return anything.
# https://stackoverflow.com/questions/3211031/python-file-read
import nltk

class ProcessText(object):
# The isCounter will be used to assign the boolean value of is category, after certain limit has passed.
# innitialTextFile is the fresh text file, that needs to be tokenized.
# textFileContent is the text file in the form of string data type.
# tokens are the string tokens fetched from the innitialTextFile.
# triggerPattern is user specified string tokens, which will increment the isCounter.
# verboseMode, when true, will obligate the ProcessText.py to verbosely explain everything that is going on.
# isCategory will have to be assigned with a True value, if the isCounter exceeds the specified limit.
    def __init__(self):
        self.isCounter = 0
        self.innitialTextFile = None
        self.textFileContent = None
        self.tokens = None
        self.triggerPattern =[]
        self.threshold = 5
        self.verboseMode = False
        self.isCategory = False
        print("ProcessText has been innitialized.")

# Prints out the content inside the textFileContent
    def printtextFileContent(self):
        print("Consumed content\n:", self.textFileContent, "\n")

# Prints out the content inside the triggerPattern
    def printTriggerPattern(self):
        print("The patterns for incrementing the counter is: ", self.triggerPattern[:])

# Prints out the content inside the isCounter
    def printIsCounter(self):
        print("Currently, the amount of counter is: ", self.isCounter)

# By comparing the tokens to the user specified patterns, increment the isCounter.
    def matchPattern(self):
        freqDist = nltk.FreqDist(self.tokens)
        for pattern in self.triggerPattern:
            if(self.verboseMode == True):
                print("Current pattern: ", pattern)
                print("Current frequency of the pattern: ", freqDist[pattern])
            self.isCounter = self.isCounter + freqDist[pattern]

# Enables the user to append a pattern to the triggerPattern list, which will be used to increment
# the isCounter, each time when the user specified pattern is found.
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
        self.innitialTextFile = open(fileName, "r")
        self.textFileContent = self.innitialTextFile.read()

# As the name suggests
    def tokenizetextFileContent(self):
        if(self.verboseMode):
            print("In the block for tokenizetextFileContent.")
        self.tokens = nltk.word_tokenize(self.textFileContent)

# Increment the isCounter separate from the matchPattern method, and string token specified by the user.
# In this case, findThis argument will be used for comparison, and the isCounter will be incremented
# according to that.
# Each time when the specified pattern is found, increase the isCounter.
    def countFrequency(self, findThis, limit=3):
        fDistObj = nltk.FreqDist(self.tokens)
        if(self.verboseMode):
            print("Consumed:", fDistObj.keys())
        amtOfOccur = fDistObj[findThis]
        #I am guessing the frequency distribution cannot consume anything aside from
        #tokenized string.
        print("The word", findThis, "has occured this much:", amtOfOccur)
        self.isCounter = self.isCounter + amtOfOccur

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
                "tokenizetextFileContent <- Tokenizes the consumed text file.\n",
                "countFrequency <- Counts the frequency of a certain string token.\n",
                "toString <- prints out all the contents within the fields of ProcessText object, with it's data type.")

    def changeThreshold(self, userInput):
        if(self.verboseMode == True):
            print("The current threshold is:", self.threshold)
        if((userInput > 0) == False):
            print("Invalid input, changing the threshold to default value 5.")
            self.threshold = 5
            return
        self.threshold = userInput

    def finalize(self):
        if(self.threshold < self.isCounter):
            self.isCategory = True
