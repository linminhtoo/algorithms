# https://leetcode.com/problems/reach-a-number/submissions/

# BFS fails cos the first time a number is reached it won't necessarily be the shortest way to reach it.
# if we need to try multiple ways to reach that number, time complexity will blow up O(2**N)
class Solution:
    def reachNumber(self, target):
        t = abs(target)
        n = math.floor(math.sqrt(2*t))
        while True:
            to_minus = ((n+1)*n)/2 - t 
            if to_minus >= 0:  
                if to_minus%2==0:
                    return int(n)
            n+=1