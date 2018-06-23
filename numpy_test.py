import numpy as np

# arri = np.array([1, 2, 3, 4])
# print(arri)
# print(arri.dtype)
#
# arr2 = np.array([1.2, 3.4, 5.6, 7.3])
# print(arr2)
# print(arr2.dtype)
# print(arri + arr2)
# print(arr2 * 10)
# date = ([1, 2, 3], [4, 5, 6])
# arr3 = np.array(date)
# print(arr3)
# print(arr3.dtype)
# print(np.zeros(10))
# print(np.ones((4, 6)))
# print(np.empty((2, 3, 2)))
arr4 = np.arange(10)
print(arr4)
print(arr4[5])
print(arr4[5:8])
arr4[5:8] = 10
print(arr4)
arr4_slice = arr4[5:8].copy()
arr4_slice[:] = 15

print(arr4)
print(arr4_slice)
