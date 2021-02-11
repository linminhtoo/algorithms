# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode('dummy')
        dummy.next = head
        
        curr = head
        prev = dummy
        while curr:
            if curr.val == val:
                # remove curr node from LinkedList
                # technically should also do this:
                # curr.next = None
                prev.next = curr.next                
            else:
                # no change to LinkedList
                # update prev to curr
                prev = curr
            curr = curr.next
            
        return dummy.next

# recursive solution in Java
# public ListNode removeElements(ListNode head, int val) {
#         if (head == null) return null;
#         head.next = removeElements(head.next, val);
#         return head.val == val ? head.next : head;
# }