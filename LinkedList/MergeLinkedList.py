# Definition for a linked-list node.
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution:
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

  def mergeTwoListsIterative(self, a, b):
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

# Test program
# 1 -> 3 ->5
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

# 2 -> 4 -> 6
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

c = Solution().mergeTwoLists(a, b)
while c:
  print(c.val)
  c = c.next
# 1 2 3 4 5 6