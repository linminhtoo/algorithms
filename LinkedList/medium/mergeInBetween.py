# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# https://leetcode.com/problems/merge-in-between-linked-lists/submissions/
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 0
        curr = head = list1
        while curr.next:
            if idx + 1 == a:
                temp = curr.next
                curr.next = list2
                curr = temp
                idx += 1
            elif idx == b:
                end = curr.next
                break
            else:
                curr = curr.next
                idx += 1
            
        curr = list2
        while curr:
            if not curr.next:
                curr.next = end
                break
            else:
                curr = curr.next
        
        return head