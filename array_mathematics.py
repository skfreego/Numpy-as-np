"""
Task :- You are given two integer arrays, A and B of dimensions NXM.
Your task is to perform the following operations:
Input Format :- The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.
Output Format :- Print the result of each operation in the given order under Task.
"""

"""
1 4
1 2 3 4
5 6 7 8
"""

import numpy
N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)



