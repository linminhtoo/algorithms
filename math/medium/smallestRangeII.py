# https://leetcode.com/problems/smallest-range-ii/discuss/?currentPage=1&orderBy=most_votes&query=
# thankfully I realized that the array needs to be sorted
# need to realize the 'boundary' between + & -, once that is done the rest is pretty trivial
class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans