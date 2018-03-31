from ProcessText import ProcessText
import sys

tagger = ProcessText()

def processOptions():
   print(sys.argv[:])
   if(len(sys.argv) > 1):
      if(sys.argv[1] == "-lf"):
         tagger.listFunctions()
      if(sys.argv[1] == "-vrb"):
         tagger.verboseModeOn()

def ready():
    while(True):
       print("Spinning...\n",
       "Please, type in the numbers for the desired action to be taken.\n",
       "1 <- print out the content of the text file.\n",
       "2 <- Find the frequency of the specific token.\n",
       "3 <- To append the pattern which increases the counter for the desired categorization.\n",
       "4 <- To list the patterns that would trigger the counter.\n",
       "5 <- Increment the counter, in accordance to the existing patterns.\n",
       "6 <- display the amount of existing patternMatchCount\n",
       "7 <- Change the value of the matchCountThreshold",
       "8 <- Display the value of the tokenCountThreshold",
       "9 <- With the current token, assign the amount of tokens to tokenCount.",
       "q <- Terminate this application.")
       select = input("Enter a number to innitiate the action (or a character) to inniate an action: ")
       processInput(select)

def processInput(userInput):
   print("You typed:", userInput)
   if(userInput == "1"):
      tagger.printtextFileContent()
   if(userInput == "2"):
      argument = input("Type in the desired token to find the frequency for: ")
      tagger.countFrequency(argument)
   if(userInput == "3"):
      tagger.addTriggerPattern(input("Type in the desired pattern which increases the counter: "))
   if(userInput == "4"):
      tagger.printTriggerPattern()
   if(userInput == "5"):
      tagger.matchPattern()
   if(userInput == "6"):
      tagger.printPatternMatchCount()
   if(userInput == "7"):
        while(True):
            usrInput = int(input("Type in the numerical value, which will replace the matchCountThreshold."))
            if(usrInput <= 0):
                print("Invalid input, the input must be bigger than ")
                continue
            taggerself.changeMatchCountThreshold(usrInput)
            return
   if(userInput == "8"):
        print("The current matchCountThreshold is:", tagger.tokenCountThreshold)
   if(userInput == "9"):
        tagger.setTokenCount()
   if(userInput == "q"):
      tagger.finalize()
      print("Terminating this application.")
      sys.exit()

if __name__ == "__main__":
   print("argvs are: ", sys.argv[:])
   if(len(sys.argv) > 2):
      processOptions()
      tagger.fileToString(sys.argv[2])
      tagger.tokenizeTextFileContent()
      ready()
   if(len(sys.argv) <= 2):
      tagger.fileToString(sys.argv[1])
      tagger.tokenizeTextFileContent()
      ready()
