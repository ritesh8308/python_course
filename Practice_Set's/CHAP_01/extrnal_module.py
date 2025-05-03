# External_Module_Used: numpy 

import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("\n1D Array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Mean, sum, and standard deviation
data = np.array([10, 20, 30, 40, 50])
print("\nStatistical Operations:")
print("Mean:", np.mean(data))
print("Sum:", np.sum(data))
print("Standard Deviation:", np.std(data))

# Define two 2D arrays
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:\n", result)
