import logging
from typing import List

class Solution:
    @staticmethod
    #  [1, 5, 9, 1, 1], 1, 1)
    def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
        ''' t = diff in number, k = diff in index 
        ABANDON
        '''
        tupled_nums = [(x, index) for index, x in enumerate(nums)]
        tupled_nums.sort(key = lambda x: (x[0], x[1]))
        
        print(tupled_nums) 
        # [(1, 0), (1, 3), (1, 4), (5, 1), (9, 2)]

        set_nums = set(nums)
        for curr_num in set_nums:
            if curr_num + k in set_nums.remove(curr_num):
                # go to tupled_nums





if __name__ == '__main__':
    Solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 1], 1, 1)
    