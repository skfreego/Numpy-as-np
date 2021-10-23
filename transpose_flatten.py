"""
Task:- You are given a N*M integer array matrix with space separated elements ( N = rows and M = columns).
Your task is to print the transpose and flatten results.
Input Format:- The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.
Output Format:- First, print the transpose array and then print the flatten.
"""

"""
2 2
1 2
3 4
"""


import numpy
n, m = map(int, input().split())

storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose())
print (storage.flatten())
