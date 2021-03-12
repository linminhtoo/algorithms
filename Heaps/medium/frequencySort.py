# https://leetcode.com/problems/sort-characters-by-frequency/submissions/
from collections import Counter, defaultdict
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s) # O(N)
        # keys = char, value = freq
        h = []
        for char, freq in counter.items():
            # -freq --> inverts the minheap to a maxheap
            heapq.heappush(h, (-freq, char)) # each append is O(logN)
        res = ""
        for _ in range(len(h)): # this can have at most N items
            freq, char = heapq.heappop(h) # each pop is O(logN)
            res += char * -freq
        return res # time complexity is O(NlogN), extra space is O(N)

class Solution_hashmap_ON:
    # somehow is slightly slower than heap solution
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        hashmap = defaultdict(list)
        for char, freq in counter.items():
            hashmap[freq].append(char * freq)
        # ''.join(list) is O(N) where N = total length of chars in list
        return ''.join(''.join(hashmap[freq]) for freq in range(len(s), -1, -1) if freq in hashmap)


if __name__ == '__main__':
    case1 = "tree"
    ans1 = "eert"

    case2 = "cccaaa"
    ans2 = "aaaccc" # heapsort is not stable, wont get "cccaaa" as the output

    case3 = "Aabb"
    ans3 = "bbAa"

    s = Solution()
    assert ans1 == s.frequencySort(case1)
    assert ans2 == s.frequencySort(case2)
    assert ans3 == s.frequencySort(case3)