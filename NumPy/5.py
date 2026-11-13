import numpy as np

#! Reorganizing Arrays

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before, before.shape)

after = before.reshape((8, 1)) #! We enter our desired shape
print(after, after.shape)

#* We can size it up to any dimension and any shape until and unless it has the same amount of values

# Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2, v1]))

# Horizontally stacking vectors
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

print(np.hstack([h1, h2, h1]))