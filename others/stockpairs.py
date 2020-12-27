#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    # Write your code here
    found = set()

    stocksProfit = sorted(stocksProfit)
    i, j = 0, len(stocksProfit) - 1 # start
    while j >= 0 and i <= len(stocksProfit) - 1:
        if i == j:
            i += 1
        stockA = stocksProfit[i]
        stockB = stocksProfit[j]
        now_sum = stockA + stockB 
        if now_sum == target:
            found.add(frozenset([stockA, stockB]))
            i += 1        

        else:
            if now_sum > target:
                j -= 1
            else:
                i += 1

    return len(found)    
 