from typing import List

class Solution:
    @staticmethod
    def rob(nums: List[int]):
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)

        grid = [[0 for i in range(len(nums))] for j in range(3)]
        grid[0][0] = nums[0]
        grid[1][0] = nums[0]
        grid[2][0] = nums[0]

        grid[0][1] = nums[1]
        grid[1][1] = nums[1]
        grid[2][1] = nums[1]

        for col_idx in range(2, len(nums)):
            if col_idx == len(nums)-1: # last house
                grid[0][col_idx] += grid[2][col_idx-2] + nums[col_idx] - nums[0]
                grid[1][col_idx] += grid[2][col_idx-1] + nums[col_idx] - nums[col_idx-1] - nums[0]
                grid[2][col_idx] += max(grid[0][col_idx], grid[1][col_idx])              
            else:
                grid[0][col_idx] += grid[2][col_idx-2] + nums[col_idx]
                grid[1][col_idx] += grid[2][col_idx-1] + nums[col_idx] - nums[col_idx-1]
                grid[2][col_idx] += max(grid[0][col_idx], grid[1][col_idx])

            
            print(grid)

        return max(grid[2][-1], grid[2][-2])

if __name__ == '__main__':
    print(Solution.rob([2, 3, 2]))
    print(Solution.rob([0]))
    print(Solution.rob([1, 2, 3, 1]))
    print(Solution.rob([2, 3, 2, 50, 2]))
    print(Solution.rob([2, 3, 2, 50, 2, 3, 1, 30, 5, 31]))