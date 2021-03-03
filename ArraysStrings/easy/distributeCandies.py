from collections import Counter
from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = Counter(candyType)
        eaten = 0
        while eaten < len(candyType) // 2 and eaten < len(candies):
            eaten += 1
            
        return eaten