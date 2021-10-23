"""
Task :- You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
Input Format :- The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.
Output Format :- Print the desired value.
"""

"""
1.1 2 3
0
"""

import numpy

poly = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(poly, x))

