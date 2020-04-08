############### Instructions ####################
## Given a 6 x 6 2D array, 'arr'
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in 'A' to be a subset of values with indices falling in this pattern in 'arr''s graphical representation:

# a b c
#   d
# e f g

# Input format
# Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].

# Print the largest (maximum) hourglass sum found in arr

# ** This is a practice on nested loops **

#!/bin/python3
import math
import os
import random
import re
import sys
import itertools

# Complete the hourglassSum function below.
# def hourglassSum(arr):

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # arr contains 2D array of input

listSumRowOne = []
for i in range(0,4):
    rowOne = arr[0][i] + arr[0][i+1] + arr[0][i+2] + arr[1][i+1] + arr[2][i] + arr[2][i+1] + arr[2][i+2]
    listSumRowOne.append(rowOne)

listSumRowTwo = []
for i in range(0,4):
    rowTwo = arr[1][i] + arr[1][i+1] + arr[1][i+2] + arr[2][i+1] + arr[3][i] + arr[3][i+1] + arr[3][i+2]
    listSumRowTwo.append(rowTwo)

listSumRowThree = []
for i in range(0,4):
    rowThree = arr[2][i] + arr[2][i+1] + arr[2][i+2] + arr[3][i+1] + arr[4][i] + arr[4][i+1] + arr[4][i+2]
    listSumRowThree.append(rowThree)

listSumRowFour = []
for i in range(0,4):
    rowFour = arr[3][i] + arr[3][i+1] + arr[3][i+2] + arr[4][i+1] + arr[5][i] + arr[5][i+1] + arr[5][i+2]
    listSumRowFour.append(rowFour)

listSum = listSumRowOne + listSumRowTwo + listSumRowThree + listSumRowFour

print(max(listSum))