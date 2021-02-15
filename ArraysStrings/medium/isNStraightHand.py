# https://leetcode.com/problems/hand-of-straights/solution/
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        hand.sort()
        curr = hand.pop(0)
        i = 0
        count = 1
        while i <= len(hand) - 1:
            if count == W:
                if hand:
                    curr = hand.pop(0)
                    count = 1
                    i = 0
                else:
                    return True
            else:                    
                if hand[i] == curr + 1:
                    curr = hand.pop(i)
                    count += 1
                elif hand[i] == curr:
                    i += 1
                else:
                    return False
        return len(hand) == 0 
        # needed. have cases where i > len(hand) - 1 
        # and we don't get to return True within while loop
        
import collections
class Solution_counter:
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True

class Solution_heapq_straightsarray:
    # follow-up is to return a 'straights' array
    def straightHands(self, hand, W):
        pq = []
        for num in hand:
            heapq.heappush(pq, num)
        straights = []
        while len(pq) > 0:
            straight = []
            dumps = []
            while len(pq) > 0 and len(straight) < W:
                pop = heapq.heappop(pq)
                if len(straight) == 0 or pop == straight[-1] + 1:
                    straight.append(pop)
                else:
                    dumps.append(pop)
            straights.append(straight)
            if len(straight) < W:
                return []
            else:
                for dump in dumps:
                    heapq.heappush(pq, dump)
        return straights