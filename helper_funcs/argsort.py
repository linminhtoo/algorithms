from typing import List
def argsort(self, seq: List[int]) -> List[int]
    return sorted(range(len(seq)), key=seq.__getitem__)