class Solution:
    def minOperations(self, n: int) -> int:
        num_ops = 0
        for i in range(0, n // 2, 1):
            num_ops += n - (2 * i + 1)
        return num_ops