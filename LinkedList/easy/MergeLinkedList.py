# Definition for a linked-list node.
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
# Definition for a linked-list node.
class ListNode(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Iterative_Solution_easy:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      head = ListNode(-100)
      curr = head
      
      while l1 and l2:
          if l1.val >= l2.val:
              curr.next = l2
              curr = l2
              l2 = l2.next
          else:
              curr.next = l1
              curr = l1
              l1 = l1.next
      
      if l1:
          curr.next = l1
      if l2:
          curr.next = l2
      
      return head.next 

class Recursive_Solution:
  def mergeTwoLists(self, a, b):
    if a is None:
      return b
    elif b is None:
      return a
    elif a.val < b.val:
      a.next = self.mergeTwoLists(a.next, b)
      return a
    else:
      b.next = self.mergeTwoLists(a, b.next)
      return b

class Iterative_Solution:
  def mergeTwoLists(self, a, b):
    node = None
    head = None
    while True:
      if a is None:
        nextNode = b
      elif b is None:
        nextNode = a
      elif a.val < b.val:
        nextNode = a
      else:
        nextNode = b

      if nextNode == a:
        a = a.next if a else None
      if nextNode == b:
        b = b.next if b else None

      if nextNode is None:
        break
      if not node:
        node = nextNode
        head = node
      else:
        node.next = nextNode
      node = nextNode
    return head

# more examples
# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python
class Solution_recursion_5lines:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

class Solution_iterative_leetcode:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr_node = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr_node.next = l1
                curr_node = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                curr_node = l2
                l2 = l2.next
        curr_node.next = l1 or l2
        # actually while loop is redundant. just need to connect once, not every single piece.
        # while l1:
        #     curr_node.next = l1
        #     curr_node = l1
        #     l1 = l1.next
        # while l2:
        #     curr_node.next = l2
        #     curr_node = l2
        #     l2 = l2.next
        return dummy.next

if __name__ == '__main__':
  # Test program
  # 1 -> 3 ->5
  a = Node(1)
  a.next = Node(3)
  a.next.next = Node(5)

  # 2 -> 4 -> 6
  b = Node(2)
  b.next = Node(4)
  b.next.next = Node(6)

  c = Recursive_Solution().mergeTwoLists(a, b)
  while c:
    print(c.val)
    c = c.next
  # 1 2 3 4 5 6