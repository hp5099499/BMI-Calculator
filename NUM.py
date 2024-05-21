# Write a Numpy program to get the Numpy version and show the Numpy build configuration. 
# import numpy as np
# print(np.__version__)
# print(np.show_config())


# Write a NumPy program to test whether none of the elements of a given array are zero
# import numpy as np

# arr=np.array([2,3,5,3,0,34])
# print(arr)
# print('Test whether none of the elements of a given array are zero')
# print(np.all(arr))

# # Write a NumPy program to test if any of the elements of a given array are non-zero.
# import numpy as np

# arr=np.array([2,3,5,3,0,34])
# print(arr)
# print('Test whether none of the elements of a given array are non-zero')
# print(np.any(arr))

# Write a NumPy program to test whether two arrays are element-wise equal within a tolerance
# import numpy as np
# arr=np.array([2,4,3,12,54])
# arr1=np.array([544,65,654,65,3])
# print(np.allclose(arr,arr1))

# Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives. 
# import numpy as np
# array =np.zeros(10)
# print(array)
# array =np.ones(10)
# print(array)
# array =np.ones(10)*5
# print(array)



# Write a NumPy program to multiply two given arrays of the same size element-by-element.
# import numpy as np
# arr=np.array([1,3,5,7,9])
# arr1=np.array([2,4,6,8,10])
# if len(arr)==len(arr1):
#   print(np.multiply(arr,arr1))
# else :
#  print('length is not same')

# Write a NumPy program to swap rows and columns of a given array in reverse order. 
# import numpy as np
# arr=np.array([[[1,2,3],[2,23,4],[23,345,634]]])
# print(arr)
# print(arr[::-1,::-1])

# Write a NumPy program to create a three-dimensional array with the shape (3,5,4) and set it to a variable.
from numpy import random
x=random.randint(100,size=(3,5,4))
print(x)

# Write a NumPy program to check whether two arrays are equal (element wise) or not.
# import numpy as np

# arr=np.array([1,3,5,7,9])
# arr1=np.array([2,4,6,8,10])
# print(np.equal(arr,arr1))

print(std())