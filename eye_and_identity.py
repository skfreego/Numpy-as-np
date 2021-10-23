"""
Task:- Your task is to print an array of size N*M with its main diagonal elements as 1's and 0's everywhere else.
Input Format:-A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.
Output Format:- Print the desired N*M array
"""

"""
3 3
"""

import numpy
numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))