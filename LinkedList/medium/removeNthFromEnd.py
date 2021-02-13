# ZC's common list!
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_single_pass:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode('dummy')
        dummy.next = head
        back, front = dummy, dummy
        counter = 0
        while counter <= n:
            front = front.next
            counter += 1

        while front:
            back = back.next
            front = front.next
            
        # remove link to Node(4) and also link FROM Node(4)
        to_delete = back.next
        back.next = back.next.next
        to_delete.next = None
        return dummy.next
        # NOTE: below doesn't work, cuts the LinkedList
        # back.next, back.next.next = back.next.next, None