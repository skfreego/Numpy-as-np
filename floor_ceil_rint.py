"""
Task :- You are given a 1-D array, A. Your task is to print the floor, celi and rint of all the elements of A.
Input Format :- A single line of input containing the space separated elements of array A.
Output Format :- On the first line, print the Floor of A.
On the second line, print the Ceil of A.
On the third line, print the Rint of A.
"""

"""
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
"""

import numpy
numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))



