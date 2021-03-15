# Course 4
# Python for Data Science, AI & Development
# 7-Objects and Classes

#Classes

# Import the library
import matplotlib.pyplot as plt
%matplotlib inline

# Create a class Circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

#Creating an instance of a class Circle
# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
dir(RedCircle)

# Print the object attribute radius
RedCircle.radius

# Print the object attribute color
RedCircle.color

# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius

# Call the method drawCircle
RedCircle.drawCircle()

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)

# Print the object attribute radius
BlueCircle.radius

# Print the object attribute color
BlueCircle.color

# Call the method drawCircle
BlueCircle.drawCircle()


#The Rectangle Class
# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 10, 'blue')

# Print the object attribute height
SkinnyBlueRectangle.height

# Print the object attribute width
SkinnyBlueRectangle.width

# Print the object attribute color
SkinnyBlueRectangle.color

# Use the drawRectangle method to draw the shape
SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

# Print the object attribute height
FatYellowRectangle.height

# Print the object attribute width
FatYellowRectangle.width

# Print the object attribute color
FatYellowRectangle.color

# Use the drawRectangle method to draw the shape
FatYellowRectangle.drawRectangle()

#Exercises
#Text Analysis
#You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods -

#Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
#freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
#freqOf - returns the frequency of the word passed in argument.
#The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise.
#Hint: Some useful functions are replace(), lower(), split(), count()

class analysedText(object):
    
    def __init__ (self, text):
        pass
    
    def freqAll(self):        
        pass
    
    def freqOf(self,word):
        pass

 import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )


class analysedText(object):

    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0