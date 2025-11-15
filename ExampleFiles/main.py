# Importing and use of NumPy
import numpy as np

# np.array - allows you to pass in a pregular python list in order to create a NumPy array
arr = np.array([1,2,3,4,5])

print(arr)

# checking numpy version
print(np.__version__)

print("")
print("")

# arrays and multidimensional arrays
a = np.array([13,4,1,32,31])
# example of a basic 2-d array
b = np.array([[1,2,3,4], [5,6,7,8]])
print(a)
print(b)
# [13  4  1 32 31]
# [[1 2 3 4]
#  [5 6 7 8]]

# using numpy for mathematics
a1 = np.array([[1,2,3,], [ 4,5,6]])
# exponential transformations
print(np.exp(a1))
# [[  2.71828183   7.3890561   20.08553692]
#  [ 54.59815003 148.4131591  403.42879349]]

#logarithm
a2 = np.array([[1,2,3,], [ 4,5,6]])
print(np.log(a2))
# [[0.         0.69314718 1.09861229]
# [1.38629436 1.60943791 1.79175947]]
