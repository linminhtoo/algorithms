# Assuming directed acyclic graph (DAG), we can use breadth-first search (BFS) from origin vertex
# every time we visit a vertex, we can add the weight of the edge to keep track of total_weight of current path
# at each vertex, we loop through all outgoing edges (since this is a directed graph) & append them to a queue
# we continue exploring vertices until we reach the vertex that has no outgoing edges, then we compare 
# total_weight to a global variable max_weight. if total_weight > max_weight, we found a better path, so 
# we update max_weight = total_weight, and then we remember this path as best_path

# here is the python code
from collections import defaultdict, deque
from typing import List, Tuple
class Graph:
  def __init__(self):
    self.vertices = set()
    self.edges = defaultdict(list)
    self.weights = {} # NOTE: weights will all be positive

  def add_vertex(self, vertex: str, weight: int) -> None:
    self.vertices.add(vertex)
    self.weights[vertex] = weight

  def add_edge(self, from_vertex: int, to_vertex: int) -> None:
    # we make directed edge
    self.edges[from_vertex].append(to_vertex)

def BFS(graph: Graph, origin: str) -> Tuple[List, int]:
    q = deque()
    max_weight = float('-inf')
    best_path = []
    q.append((origin, graph.weights[origin], [origin])) # Tuple[vertex, total_weight, current_path]
    while q:
        curr_v, curr_weight, curr_path = q.popleft()
        
        if len(graph.edges[curr_v]) > 0: # at least 1 outgoing edge from current_vertex
            for next_v in graph.edges[curr_v]:
                total_weight = curr_weight + graph.weights[next_v]
                new_path = curr_path + [next_v]
                q.append((next_v, total_weight, new_path))
        else: # no outgoing edges, terminate current path
            if curr_weight > max_weight:
                max_weight = curr_weight
                best_path = curr_path

    return best_path, max_weight

# However, the key assumption is that graph is acyclic, meaning it is impossible to visit
# a vertex we have already explored. This ensures that every BFS-path MUST terminate at some point when 
# vertex.outgoing_edges = None

# If graph is no longer acyclic, it is possible for vertex's outgoing edge to point back to a vertex we already visited
# this will cause infinite loop since there will be some BFS-path that will never hit the termination criteria (vertex.outgoing_edges = None)
# To overcome this, we can keep track of vertices we already visited so far using a set, visited = set()
# When we append new edge, we ensure the vertex we are visiting is not already in the visited set.
# the new termination criteria is when either vertex.outgoing_edges = None OR when vertex.children_vertex are all in visited set.

# we also have to change to recursive with backtracking so that visited set only applies for this particular path
# here is modified code that works
from copy import deepcopy
class Solution:
    def DFS(self, graph: Graph, origin: str) -> Tuple[List, int]:
        self.max_weight = float('-inf')
        self.best_path = []
        
        def helper(vertex, weight, path, visited):
            if weight > self.max_weight:
                self.max_weight = weight
                self.best_path = path

            for next_v in graph.edges[vertex]:
                if next_v not in visited:
                    new_visited = deepcopy(visited)
                    new_visited.add(next_v)
                    total_weight = weight + graph.weights[next_v]
                    new_path = path + [next_v]

                    helper(next_v, total_weight, new_path, new_visited)

        helper(origin, graph.weights[origin], [origin], set([origin]))
        return self.best_path, self.max_weight                

# realized BFS doesnt work if graph is cyclic!!!
# def BFS_with_visited(graph: Graph, origin: str) -> Tuple[List, int]:
#     q = deque()
#     max_weight = float('-inf')
#     best_path = []
#     q.append((origin, graph.weights[origin], [origin])) # Tuple[vertex, total_weight, current_path]
#     visited = set([origin]) # add origin to visited
#     while q:
#         curr_v, curr_weight, curr_path = q.popleft()

#         # slightly modified this part, so we check curr_weight at every new vertex
#         # bcos we don't know if all children vertex are already visited
#         if curr_weight > max_weight:
#             max_weight = curr_weight
#             best_path = curr_path
        
#         if len(graph.edges[curr_v]) > 0:
#             # at least 1 outgoing edge from current_vertex AND next_v is not in visited set
#             for next_v in graph.edges[curr_v]:
#                 if next_v not in visited:
#                     visited.add(next_v) # add next_v to visited set
#                     total_weight = curr_weight + graph.weights[next_v]
#                     new_path = curr_path + [next_v]
#                     q.append((next_v, total_weight, new_path))

#     return best_path, max_weight

if __name__ == '__main__':
    g = Graph()
    # test directed acyclic graph
    g.add_vertex('A', 1)
    g.add_vertex('B', 2)
    g.add_vertex('C', 2)

    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('A', 'C')

    print(BFS(g, 'A')) # outputs (['A', 'B', 'C'], 5)

    # test directed cyclic graph
    g = Graph()
    g.add_vertex('A', 1)
    g.add_vertex('B', 2)
    g.add_vertex('C', 2)

    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('A', 'C')
    g.add_edge('C', 'A') # cyclic connection

    solution = Solution()
    print(solution.DFS(g, 'A')) # outputs (['A', 'B', 'C'], 5)


