# https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/265508/JavaC%2B%2BPython-Next-Greater-Element
class Solution:
    def nextLargerNodes(self, head):
        res, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        return res

# O(N^2) time complexity doesn't pass :( 
#         if not head:
#             return []
        
#         out = []
#         curr = head
#         while curr:
#             explorer = curr.next
#             while explorer and explorer.val <= curr.val:
#                 explorer = explorer.next
#             if explorer:
#                 out.append(explorer.val)
#             else:
#                 out.append(0)
#             curr = curr.next
            
#         return out