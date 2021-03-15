# Course 4
# Python for Data Science, AI & Development
# 12- Two Dimensional Numpy

#Create a 2D Numpy Array

# Import the libraries
import numpy as np 
import matplotlib.pyplot as plt

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A

# Show the numpy array dimensions
A.ndim

# Show the numpy array shape
A.shape

# Show the numpy array size
A.size

#Accessing different elements of a Numpy Array

# Access the element on the second row and third column
A[1, 2]

# Access the element on the second row and third column
A[1][2]

# Access the element on the first row and first column
A[0][0]

# Access the element on the first row and first and second columns
A[0][0:2]

# Access the element on the first and second rows and third column
A[0:2, 2]

#Basic Operations

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y
Z = X + Y
Z

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Multiply Y with 2
Z = 2 * Y
Z

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Multiply X with Y
Z = X * Y
Z

# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
A

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
B

# Calculate the dot product
Z = np.dot(A,B)
Z

# Calculate the sine of Z
np.sin(Z)

# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C

# Get the transposed of C
C.T

#Quiz on 2D Numpy Array

# Write your code below and press Shift+Enter to execute
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
A

#Calculate the numpy array size.
A.size


#Access the element on the first row and first and second columns.
A[0][0:2]

#Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
X = np.dot(A,B)
X