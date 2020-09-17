# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# 74% faster, 74% less memory 
class IterativeSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = head
        now = prev.next 
        if prev is None:
            return None
        if prev.next is None:
            return prev
        
        future = now.next
        prev.next, now.next = None, prev
        
        while future:
            prev, now = now, future 
            future, now.next = now.next, prev
        return now 

class IterativeSolution_short():
    def reverseList(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

class RecursiveSolution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
        