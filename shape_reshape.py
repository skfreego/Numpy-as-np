"""
Task :-You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
Input Format:- A single line of input containing 9 space separated integers.
Output Format:- Print the 3X3 NumPy array.
"""

"""
1 2 3 4 5 6 7 8 9
"""

import numpy

print(numpy.array(input().split(), int).reshape(3, 3))

