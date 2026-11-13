import numpy as np

#! Miscellaneous

# Load data from from file
filedata = np.genfromtxt("data.txt", delimiter=",")
print(filedata)
filedata = filedata.astype("int32")
print(filedata)

# Advanced Indexing & Boolean Masking
print(filedata > 50)
print(filedata[filedata > 50])

# You can index with List in NumPy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]]) #! We pass indexes in the list

print(np.any(filedata > 50, axis=0))
print(np.any(filedata > 50, axis=1))

print(np.all(filedata > 50, axis=0))
print(np.all(filedata > 50, axis=1))

print((filedata > 50) & (filedata < 100)) # Greater than 50 AND Less than 100
print(~(filedata > 50) & (filedata < 100)) # NOT Greater than 50 AND Less than 100