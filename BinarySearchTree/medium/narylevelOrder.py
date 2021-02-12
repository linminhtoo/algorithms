# https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    # very similar to binary levelOrder traversal
    # just that we append all curr.children to q instead of doing curr.left & curr.right
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = [root]
        while q:
            lvl_res = []
            lvl_cnt = len(q)
            while lvl_cnt:
                curr = q.pop(0)
                lvl_res.append(curr.val)
                for child in curr.children:
                    q.append(child)
                lvl_cnt -= 1
            res.append(lvl_res)
        return res

class Solution_BFS_alternative:
    def levelOrder(self, root):
        output, queue = [], [root] if root else []
        while queue:
            output.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return output

# java, DFS
# class Solution {
#     public List<List<Integer>> levelOrder(Node root) {
#         return levelOrder(root, new ArrayList<>(), 0);
#     }

#     private List<List<Integer>> dfs(Node node, List<List<Integer>> res, int level) {
#             if (node == null) return res;
#             if (res.size() == level) res.add(new ArrayList<>());
#             res.get(level).add(node.val);
#             for (Node child : node.children) dfs(child, res, level + 1);
#             return res;
#     }