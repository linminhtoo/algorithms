# https://leetcode.com/problems/split-linked-list-in-parts/submissions/
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return [None] * k
        
        length = 1
        curr = root
        while curr.next:
            curr = curr.next
            length += 1
        
        q, r = divmod(length, k)
        res = []
        curr = root
        while curr:
            added, target = 1, q + (r>0) # boolean evaluated
            res.append(curr) # head of new part
            while added < target: # find the tail
                curr = curr.next
                added += 1
            # cut the tail
            curr.next, curr = None, curr.next # avoid need for temp
            r -= 1
            
        if len(res) < k:
            res.extend([None] * (k - len(res)))
        return res
        