# https://leetcode.com/problems/rotate-list/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        elif not head.next:
            return head
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        k = length - (k % length) # bcos we don't reverse the LinkedList
        # otherwise, very difficult to keep track of before_tail (whose next is to become None)
        # since before_tail moves backwards by 1 (unless we reverse the LinkedList to keep track)
        
        done = 0
        tail = curr
        while done < k:
            new_head = head.next
            tail.next, head.next = head, None 
            tail, head = tail.next, new_head
            done += 1
            
        return new_head
        
class Solution_smarter: 
    # the idea of forming a cyclic list and then breaking just 1 link is smart!
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer