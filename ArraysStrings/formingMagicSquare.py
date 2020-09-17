#!/bin/python3

import math
import os
import random
import re
import sys

# sample solution
input_nums = []
input_nums.extend([int(i) for i in input().split()])
input_nums.extend([int(i) for i in input().split()])
input_nums.extend([int(i) for i in input().split()])

#input_nums[0], input_nums[1], input_nums[2] = [int(i) for i in input().split()]
#input_nums[3], input_nums[4], input_nums[5] = [int(i) for i in input().split()]
#input_nums[6], input_nums[7], input_nums[8] = [int(i) for i in input().split()]
#print(input_nums)
pos = []
pos.append([8,1,6,3,5,7,4,9,2])
pos.append([6,1,8,7,5,3,2,9,4])
pos.append([4,9,2,3,5,7,8,1,6])
pos.append([2,9,4,7,5,3,6,1,8])
pos.append([8,3,4,1,5,9,6,7,2])
pos.append([4,3,8,9,5,1,2,7,6])
pos.append([6,7,2,1,5,9,8,3,4])
pos.append([2,7,6,9,5,1,4,3,8])

mindiff = 10000

for arr in pos:
    diff = 0
    for i in range(9):
        diff += abs(arr[i] - input_nums[i])
    if (diff < mindiff):
        mindiff = diff
        
print(mindiff)


'''
PROBLEM: the output matrices of rotateMultiple all end up becoming the same. no idea why
'''

# Complete the formingMagicSquare function below.
def formingMagicSquare(s, N=3):
    ''' 
    N : int (Default = 3)
        Size of the square 
    '''
    seed = [[6, 7, 2], [1, 5, 9], [8, 4, 3]]
    magic_squares = []
 
    for i in magic_squares:
        print(i, end='\n')
    # print('reflecting...')
    # magic_squares = magic_squares + [reflectMatrix(matrix, N) 
    #                                 for matrix in magic_squares]
    
    # for i in magic_squares:
    #     print(i, end='\n')
    

def rotateMatrix(s, N=3):
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):
            temp = s[x][y]
            s[x][y] = s[N-1-y][x]
            s[N-1-y][x] = s[N-1-x][N-y-1]
            s[N-1-x][N-y-1] = s[y][N-1-x]
            s[y][N-1-x] = temp
    return s
       
       
def rotateMultiple(s, N=3, K=1):
    '''
    K : int
        How many times to rotate the matrix
    '''
    out = []
    out.append(rotateMatrix(s))
    if K == 1:
        return out
    out.append(rotateMatrix(rotateMatrix(s)))
    if K == 2:
        return out
    out.append(rotateMatrix(rotateMatrix(rotateMatrix(s))))
    if K == 3:
        return out
    out.append(rotateMatrix(rotateMatrix(rotateMatrix(rotateMatrix(s)))))
    return out

def reflectMatrix(s, N=3):
    for x in range(0, N):
        for y in range(0, int(N/2)):
            temp = s[x][y]
            s[x][y] = s[x][N-y-1]
            s[x][N-y-1] = temp
    return s 

# formingMagicSquare(0)
seed = [[6, 7, 2], [1, 5, 9], [8, 4, 3]]