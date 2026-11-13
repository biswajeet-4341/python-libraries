import numpy as np

#! Mathematics

a = np.array([1, 2, 3, 4])
print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)

b = np.array([1, 0, 1, 0])
print(a + b)

# Take the sin/cos
print(np.sin(a))
print(np.cos(a))

#! Linear ALgebra

# Matrix Multiplication
a = np.ones((2, 3))
b = np.full((3, 2), 2)

print(np.matmul(a, b)) 

# Determinant
c = np.identity(3)
print(np.linalg.det(c))

#* We can also do the following operations using numpy. Like: Trace, Singular Vector Decomposition, Eigen Values, Matrix Norm, Inverse etc...

#* Search for NumPy documentatin online or the video has some links in the description.

#! Statistics

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(stats)

print(np.min(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))

print(np.max(stats))
print(np.max(stats, axis=0))
print(np.max(stats, axis=1))

#! Remember, axis=0 is rows and axis=1 is columns

print(np.sum(stats))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))