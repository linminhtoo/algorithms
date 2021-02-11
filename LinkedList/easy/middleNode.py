# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        counter = 0
        curr = head
        while curr.next:
            curr = curr.next
            counter += 1
        
        curr = head
        now_idx = 0
        dest_idx = counter / 2 if counter % 2 == 0 else counter // 2 + 1 
        while now_idx != dest_idx:
            curr = curr.next
            now_idx += 1
        
        return curr

class Solution_slow_and_fast_pointer:
    # fast travels 2x as fast as slow
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow