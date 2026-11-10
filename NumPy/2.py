import numpy as np

#! Accessing/Changing specific elements, rows, columns, etc.

a = np.array([[34, 2, 4, 6, 8, 24, 67], [45, 67, 2, 6, 9, 39, 69]])
print(a)
print(a.shape)

# Get a specific element [r, c]
print(a[1, 5])
print(a[1, -2])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 2])

#! ":" is used to capture all the elements of that dimension

# Getting a little more fancy [startindex : endindex(exclusive) : stepsize]
print(a[0, 1:6:2])
print(a[0, 1:-1:2])

# Changing elements
a[1, 5] = 20
print(a)

a[:, 2] = 5
print(a)
a[:, 2] = [1, 3] #! Depends on how many items are getting selected
print(a)

# 3D example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(b.ndim)
print(b.shape)

print(b[0, 1, 1]) #! <--|
print(b[:, 1, 1]) #! <--|-- Somewhat similar to normal Python lists (work outside in)
print(b[:, 1, :]) #! <--|

# Replacing/Changing elements (somewhat similar to what we do in 2D)
b[:, 1, :] = 8
print(b)
b[:, 1, :] = [[8, 8], [9, 9]]
print(b)