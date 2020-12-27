from collections import deque 

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = deque()


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.store.append(timestamp)
        # did not improve space
        # while self.store and timestamp - self.store[0] >= 300:
        #     self.store.popleft()        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.store: return 0
        while self.store and timestamp - self.store[0] >= 300:
            self.store.popleft()   

        return len(self.store)