from Typing import List

# refer to https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter4/41RouteBetweenNodes.py

class Node(object):
    def __init__(self, name: int, children: List[int]):
        self.name = name
        self.children = children
        self.visited = False

class Graph(object):
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

class Solution(object):
    def search(self, start_node: Node, end_node: Node):
        if not start_node:
            return False
        elif start_node.name == end_node.name:
            return True
        else:
            start_node.visited = True
        
        for child in start_node.children:
            if not child.visited:
                self.search(child, end_node)
        
        return False
