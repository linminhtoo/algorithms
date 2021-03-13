# https://leetcode.com/discuss/general-discussion/1066206/introduction-to-trie
# https://leetcode.com/problems/implement-trie-prefix-tree/
# https://medium.com/@prefixyteam/how-we-built-prefixy-a-scalable-prefix-search-service-for-powering-autocomplete-c20f98e2eff1
class Trie:
    def __init__(self):
        self.root = {} # see below for defaultdict implementation

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        curr_node['#'] = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]
        return '#' in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]
        return True

from collections import defaultdict
_trie = lambda: defaultdict(_trie)
# https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
class Trie_: # slightly faster than above
    def __init__(self):
        self.root = _trie()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word: # no need to check if curr_node[char] alr exists or not
            curr_node = curr_node[char]
        curr_node['#'] = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]
        return '#' in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]
        return True