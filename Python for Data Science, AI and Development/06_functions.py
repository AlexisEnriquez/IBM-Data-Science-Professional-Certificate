# Course 4
# Python for Data Science, AI & Development
# 6-Functions

#Functions

# First function example: Add 1 to a and store as b
def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Get a help on add function
help(add)

# Call the function add()
add(1)

# Call the function add()
add(2)

# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# Use mult() multiply two integers
Mult(2, 3)

# Use mult() multiply two floats
Mult(10.0, 3.14)

# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")

# Function Definition
def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

#We can call the function with an input of 3
# Initializes Global variable  
x = 3
# Makes function call and return function a y
y = square(x)
y

#We can call the function with an input of 2 in a different manner:
# Directly enter a number as parameter
square(2)


#If there is no return statement, the function returns None.
#The following two functions are equivalent:

# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output
MJ()

# See the output
MJ1()

# See what functions returns are
print(MJ())
print(MJ1())

# Define the function for combining strings
def con(a, b):
    return(a + b)

# Test on the con() function
con("This ", "is")



#Consider the two lines of code in Block 1 and Block 2: the procedure for each block 
#is identical. The only thing that is different is the variable names and values.

# a and b calculation block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1

# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c)

#BLock 3
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1

#BLock 4
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2

#Pre-defined Functions

# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# Use sum() to add every element in a list or tuple together
sum(album_ratings)

# Show the length of the list or tuple
len(album_ratings)

#Using if/else Statements and Loops in Functions

# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])

#Setting default argument values in your custom functions

# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)

#Global variables

# Example of global variable
artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 


artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

#Scope of a Variable

# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)


# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)


#Collections and Functions

#When the number of arguments are unknown for a function, 
#They can all be packed into a tuple as shown:
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

#Similarly, The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    
#Functions can be incredibly powerful and versatile. 
#They can accept (and return) data types, objects and even other functions as arguements.
#Consider the example below:
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList


#Quiz on Functions
#Come up with a function that divides the first input by the second input:
def div(a, b):
    return(a/b)

# Use the con function for the following question
def con(a, b):
    return(a + b)

#Can the con function we defined before be used to add two integers or strings?
con(2, 2)

#Can the con function we defined before be used to concatenate lists or tuples?
con(['a', 1], ['b', 1])

#Probability Bag

#You have been tasked with creating a lab that demonstrates the basics of probability 
#by simulating a bag filled with colored balls. 
#The bag is represented using a dictionary called "bag", 
#where the key represents the color of the ball and the value represents the no of balls. 
#The skeleton code has been made for you, do not add or remove any functions. 
#Complete the following functions -

#fillBag - A function that packs it's arguments into a global dictionary "bag".
#totalBalls - returns the total no of balls in the bucket
#probOf - takes a color (string) as argument and returns probability of drawing the selected ball. Assume total balls are not zero and the color given is a valid key.
#probAll - returns a dictionary of all colors and their corresponding probability

def fillBag(**balls):
    pass
     

def totalBalls():
    pass
    
def probOf(color):
    pass

def probAll():
    pass


testBag = dict(red = 12, blue = 20, green = 14, grey = 10)
total =  sum(testBag.values())
prob={}
for color in testBag:
    prob[color] = testBag[color]/total;

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("fillBag : ")
try:
    fillBag(**testBag)
    print(testMsg(bag == testBag))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")



print("totalBalls : ")
try:
    print(testMsg(total == totalBalls()))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probOf")
try:
    passed = True
    for color in testBag:
           if probOf(color) != prob[color]:
                passed = False
        
    print(testMsg(passed) )
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probAll")
try:
    print(testMsg(probAll() == prob))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")

#Functions
def fillBag(**balls):
    global bag
    bag = balls

def totalBalls():
    total = 0
    for color in bag:
        total += bag[color]
    return total
    # alternatively,
    # return sum(bag.values())

def probOf(color):
    return bag[color]/totalBalls()

def probAll():
    probDict = {}
    for color in bag:
        probDict[color] = probOf(color)
    return probDict