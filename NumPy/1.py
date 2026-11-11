import numpy as np

#! The Basics

a = np.array([1, 2, 3], dtype="int8") #! int8 is 8 bits ot 1 byte of data
print(a)

b = np.array([[9.0, 3.0, 5.0], [6.0, 5.0, 4.0]])
print(b)

# Get Dimension 
print(a.ndim)
print(b.ndim)

# Get Shape (row, columns)
print(a.shape)
print(b.shape)

# Get Data Type
print(a.dtype)
print(b.dtype)

# Get Size (in bytes)
print(a.itemsize)
print(b.itemsize)

# Get Total Size
print(a.size * a.itemsize) #! a.size gives the total number of elements in the array
print(a.nbytes)
print(b.nbytes)