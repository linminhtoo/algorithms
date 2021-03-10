# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import gc
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a, b = headA, headB
        gc.collect()
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a