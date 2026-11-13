import numpy as np

#! Initializing Different Types of Arrays

# All 0s matrix
print(np.zeros((2, 3, 3, 2))) #! Takes shapes as arguments

# All 1s matrix
print(np.ones((2, 3, 3, 2), dtype="int8")) # Specifying data type isnn't compulsory

# Any other number
print(np.full((2, 2), 99, dtype="float32")) #! np.full(shape, value)

a = np.array([[34, 56, 89, 23], [45, 78, 12, 98]])
print(np.full(a.shape, 4))
print(np.full_like(a, 4)) #! Takes a variable rather than it's shape

# Random decimal numbers
print(np.random.rand(4, 2, 3)) #! We pass the shape directly (not as a tuple)
print(np.random.random_sample(a.shape)) #! Here we pass the shape (as a tuple)

# Random integer values 
print(np.random.randint(4, 7, size=(3, 3))) #! np.random.randint(startvalue, endvalue(exclusive), size=(r, c))

# The identity matrix
print(np.identity(4))

# Repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0) #! By default axis is 1 (horizontal/columns), axis=0 makes it repeat vertically (row wise) in a 2D matrix
print(r1)

#! NOTE: Be careful when copying arrays!!!
arr1 = np.array([1, 2, 3])
arr2 = arr1.copy() #! arr2 = arr1 just makes arr2 a pointer of arr1 and any changes in arr2 changes the original values in arr1
arr2[0] = 100

print(arr1, arr2)