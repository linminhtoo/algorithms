from collections import deque
class LRUCache:
    # time complexity is bad, though space is prolly the best
    # faster than 5% only, memory better than 99.8%
    def __init__(self, capacity: int):
        self.queue = deque()
        self.data = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            while key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            # print(f'get {key}, {self.queue}, {self.data}')
            return self.data[key]
        else:
            # print(f'get {key}, {self.queue}, {self.data}')
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            # slow, O(N) in worst-case?
            while key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
        else:
            self.data[key] = value
            self.queue.append(key)
            if len(self.data) > self.cap:
                key_pop = self.queue.popleft()
                del self.data[key_pop]
        # print(f'put {key}, {value}, {self.queue}, {self.data}')

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache_dict_doublelinkedlist:
    # O(1) time to get & put
    # but need more extra space for the doubly linkedlist 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
                
    def _add(self, node: Node) -> None:
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.next = self.tail
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # this doesnt work, since we need to retrieve the exact Node that was placed
            # node = Node(key, value) 
            # so, our cache needs to store (key,Node) pairs, not (key,value) pairs
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache) > self.capacity:
            del self.cache[self.head.next.key]
            self._remove(self.head.next)

from collections import OrderedDict
class LRUCache_ordereddict:
    # shortest since we use python built-in, beats 97%
    # space is not too bad also, beats 89%
    # ordereddict rmbrs order that we put key inside
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)