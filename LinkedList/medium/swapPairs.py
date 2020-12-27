# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution_mine_iterative: # pass, but not the fastest/most concise
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = ListNode(None) # dummy node for 1st iter
        head_to_return = head.next
        while head.next:
            now = head.next
            temp = now.next # can be None
            now.next = head
            head.next = temp # can be None
            tail.next = now # join prev head (1st iter is dummy node)
            tail = head
            if head.next:
                head = head.next
        return head_to_return

class Solution_faster_recursive_readable:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node

class Solution_sametime_recursive:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        next_next = self.swapPairs(head.next.next)

        new_head = head.next
        head.next = next_next
        new_head.next = head
        return new_head

class Solution_fastest_but_invalid: 
    # modifies node.val instead of node.next, so this is invalid 
    # still, it works, and is conceptually intuitive
    def swapPairs(self, head: ListNode) -> ListNode:
        self.swapPairsHelper(head)
        return head
    
    def swapPairsHelper(self, curHead) -> None:
        if not curHead or not curHead.next:
            return
        curHead.val, curHead.next.val = curHead.next.val, curHead.val
        self.swapPairsHelper(curHead.next.next)