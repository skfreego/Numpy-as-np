"""
Task:- You are given two integer arrays of size NXP and MXP ( N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
Input Format:- The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.
Output Format:- Print the concatenated array of size (N+M)XP.
"""

"""
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
"""


import numpy
P, N, M = map(int,input().split())
A = numpy.array([input().split() for _ in range(P)],int)
B = numpy.array([input().split() for _ in range(N)],int)
print(numpy.concatenate((A, B), axis = 0))



