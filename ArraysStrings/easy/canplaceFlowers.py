from typing import List
# https://leetcode.com/problems/can-place-flowers/
class Solution_optimized:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = len(flowerbed)
        bed = [0] + flowerbed + [0] # trick is to add [0] at both front and back
        
        for i in range(1, s+1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                bed[i] = 1
                n -= 1
            
            if n <= 0: return True
        
        return False

class Solution_pass_but_not_so_fast:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n > 1: 
                return False
            elif n == 1 and flowerbed[0] == 1:
                return False
            else:
                return True
        
        count = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1 # place at 0th position
            flowerbed[0] = 1
        i = 2
        while i + 1 <= len(flowerbed) - 1:
            if flowerbed[i] == 1:
                i += 1
            
            elif flowerbed[i] == 0:
                if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    count += 1
                    flowerbed[i] = 1
                i += 1
                
            # print(i, count)
          
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1
        return count >= n