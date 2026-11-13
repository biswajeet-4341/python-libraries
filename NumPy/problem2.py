import numpy as np

#! Problem 2

mat = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]])
print(mat)

# How do you index [11, 12, 16, 17] from the given matrix?
print(mat[2:4, 0:2])

# Index [2, 8, 14, 20]
print(mat[[0, 1, 2, 3], [1, 2, 3, 4]]) #! First we provided the indexes for the rows, then for the columns

# Index [4, 5, 24, 25, 29, 30]
print(mat[[0, 4, 5], 3:])

#* There are many ways to index all of these. These are just some few ways to solve the questions to understand the usecase of every functionality.