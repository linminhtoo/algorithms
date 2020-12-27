# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# https://leetcode.com/problems/linked-list-random-node/solution/
import random
class Solution_unknown_length: 
    # reservoir sampling (algorithm R)
    # but not optimized, O(N) for sampling a number
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            # random.random() samples from [0, 1)
            # equiv to random.sample_from_[0,scope) < k, where k = 1
            # i.e. P = k / i = 1 / (scope-1), sample from [0, scope-1]
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value

class Solution_fast_but_need_space: 
    # but caveat: need space to keep pool of elements for sampling
    # means cannot deal w/ unlimited LinkedList (streaming)
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        pick = int(random.random() * len(self.range))
        return self.range[pick]


class Solution_mine: # not so fast - better to convert LinkedList to array in __init__
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        curr_node = head
        self.length = 1
        while curr_node.next:
            curr_node = curr_node.next
            self.length += 1
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        picked = random.choice(range(self.length))
        i = 0
        curr_node = self.head
        while i < picked:
            curr_node = curr_node.next
            i += 1
        return curr_node.val            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()