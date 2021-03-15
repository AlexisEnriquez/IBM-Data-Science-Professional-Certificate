# Course 4
# Python for Data Science, AI & Development
# 11- One Dimensional Numpy

# Preparation

# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

# Create a python list

a = ["0", 1, "two", "3", 4]

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#What is Numpy?

# import numpy library
import numpy as np 

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#Type

# Check the type of the array
type(a)

# Check the type of the values stored in numpy array
a.dtype

# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Check the type of array
type(b)

# Check the value type
b.dtype

#Assign Value

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
c

# Assign the first element to 100
c[0] = 100
c

# Assign the 5th element to 0
c[4] = 0
c

#Slicing

# Slicing the numpy array
d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c

#Assign Value with List
# Create the index list
select = [0, 2, 3]

# Use List to select elements
d = c[select]
d

# Assign the specified elements to new value
c[select] = 100000
c

#Other Attributes

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array
a.size

# Get the number of dimensions of numpy array
a.ndim

# Get the shape/size of numpy array
a.shape

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
mean

# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b

# Get the biggest value in the numpy array
max_b = b.max()
max_b

# Get the smallest value in the numpy array
min_b = b.min()
min_b

#Numpy Array Operations

#Array Addition
#Consider the numpy array u:

u = np.array([1, 0])
u

#Consider the numpy array v:
v = np.array([0, 1])
v

#We can add the two arrays and assign it to z:

# Numpy Array Addition
z = u + v
z

#The operation is equivalent to vector addition:
# Plot numpy arrays

Plotvec1(u, z, v)

#Array Multiplication
#Consider the vector numpy array y:

# Create a numpy array

y = np.array([1, 2])
y

# Numpy Array Multiplication

z = 2 * y
z

#Product of Two Numpy Arrays
#Consider the following array u:

# Create a numpy array

u = np.array([1, 2])
u

# Create a numpy array

v = np.array([3, 2])
v

# Calculate the production of two numpy arrays

z = u * v
z

#Dot Product

#The dot product of the two numpy arrays u and v is given by:

# Calculate the dot product

np.dot(u, v)

#Adding Constant to a Numpy Array

#Consider the following array:

# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u

# Add the constant to array

u + 1

#Mathematical Functions
#We can access the value of pi in numpy as follows :

# The value of pi
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements

y = np.sin(x)
y

#Linspace

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)


# Makeup a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# Makeup a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)

#Quiz on 1D Numpy Array
#Implement the following vector subtraction in numpy: u-v

# Write your code below and press Shift+Enter to execute
u = np.array([1, 0])
v = np.array([0, 1])
u - v

#Multiply the numpy array z with -2:
# Write your code below and press Shift+Enter to execute
z = np.array([2, 4])
-2 * z

#Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1], 
#and cast both lists to a numpy array then multiply them together:
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
a * b

#Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. 
#Then, plot the arrays as vectors using the fuction Plotvec2 and find the dot product:
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))

#Convert the list [1, 0] and [0, 1] to numpy arrays a and b.
#Then, plot the arrays as vectors using the function Plotvec2 and find the dot product:
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

#Convert the list [1, 1] and [0, 1] to numpy arrays a and b.
#Then plot the arrays as vectors using the fuction Plotvec2 and find the dot product:
a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))
print("The dot product is", np.dot(a, b))