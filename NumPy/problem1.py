import numpy as np

#! Problem 1

# Build given matrix using intialization functions
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

output = np.ones((5, 5))
print(output)

output[1:-1, 1:-1] = np.zeros((3, 3))
print(output)

output[2, 2] = 9
print(output)