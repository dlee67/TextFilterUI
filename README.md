# TextFilterUI
This application classifies the text file under a user specified category.

# What do you mean?
Under the assumption that I have an ML algorithm trained with bunch of text files (could be e-mails, could be books, etc...), classfied in binary manner, when the new text file is fed to it, the application guesses which category the text file belongs to (where the category must be user specified).

# Okay, how does it work?
Each text files will be deciphered as a 0, or 1, in accordance to the user's specified pattern (ofcourse, this includes regex). Each time when user specified pattern is detected in the text file being processed, isCounter is incremented. When the isCounter exceeds the certain amount of value, it will be flagged as either of the binary number, which is later processed in the machine learning algorithm.

# You are being extremly vague.
And here is the architecture below.
![Screenshot](Plan.png)

# I thought you didn't like Python?
I don't like certain traits about it (like, needing to care about the whitespace), but I think it's a great language.

# 03/30/18
Not sure if nltk.FreqDist() can count frequency of the pattern according to the regex pattern because when *[A-Za-z]
is used to count up the isCounter, the tester.py fails.

# 03/31/18
The code became much more "cleaner," and added a new class variable called tokenCount because the ML algorithm
I am about to feed the data to needs values representable as x-axis value and y-axis value.
I think the ProcessText.py, main.py, and the ProcessTextTester.py are completed enough?

# 04/06/18
From the looks of things, there needs to be an interface that utilizes the functions in MLAlg now.
To be conclusive about things, I still don't fully grasp how this application can be interacted with the end users.

# 04/09/18
This project will go into a hibernation.
