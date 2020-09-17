from collections import OrderedDict
from typing import List

# The main idea is to hash numbers to buckets by floor dividing the number by t.
# For example, if our current number is 9 and t is 3, then {6, 7, 8, 9, 10, 11, 12} are the almost duplicates. 
# We floor divide these nums by t into their respective buckets {2, 2, 2, 3, 3, 3, 4}. 
# They all hash to the inclusive range [2, 4] which is [num // t - 1, num // t + 1]. 
# The only caveat is that the numbers 13 and 14 also hash to bucket 4 so we have to add an extra check 
# that the absolute difference between current num and complement are less than or equal to t.

class Solution:
    @staticmethod
    #  [1, 5, 9, 1, 1], 1, 1)
    def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
        '''CORRECT SOLUTION 
        '''
        window = OrderedDict() # <bucket>: <value>
        
        for num in nums:
            if len(window) > k:
                window.popitem(last=False) # popleft

            bucket = num // (t or 1) # all candidate nums will hash to this bucket. or 1 for division by zero case
            for complement in range(bucket - 1, bucket + 2):
                if complement in window and abs(num - window[complement]) <= t:
                    return True
            
            window[bucket] = num
            
        return False