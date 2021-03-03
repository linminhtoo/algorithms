# https://leetcode.com/problems/keys-and-rooms/submissions/
from typing import List
from collections import deque
class Solution:
    # time complexiy is O(N + E) bcos we need to visit every edge(key)
    # even if room has been visited, we must visit the edge to check this
    # if room has no keys, we still needed to visit that room (the act of q.popleft())
    # so, total N + E
    # space complexity is O(N) to keep the visited set & queue
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # lets use BFS
        # there may be cycles, so we need a visited set()
        visited = set([0]) # room_number aka idx of rooms, we add 0 bcos we always visit 0 first
        q = deque([0]) # list of rooms we can visit
        while q:
            room = q.popleft()
            # print(room, visited, q)
            
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return len(visited) == len(rooms)