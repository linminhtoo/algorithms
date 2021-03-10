from collections import defaultdict
from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # attach # to every word in words
        # build our encoding output word by word
        # check if word already exists in encoding, if not then append it to encoding
        # O(N^2)?
        
        # for each word[i], check if it already exists in our current encoding
        # e.g. 'me#' exists in 'time#bell#'
        # so, we just retrieve the value from dictionary, dict['me#'] = 2
        # otherwise, (not present in dictionary)
        # for each word[i], we can fragment it up to 7 valid ways
        # e.g. time --> time# --> time#, ime#, me#, e#
        # put all these in a dictionary, with value = index of fragmentation + length of encoding so far
        # e.g. {'time#': 0, 'ime#': 1, 'me#': 2, 'e#': 3} (length of encoding = 0 at this point)
        # need to first sort words by length (longest first --> shortest)
        # O(N) * O(k**2) = O(49N)

        words.sort(key=len, reverse=True)
        
        res = ""
        indices = []
        seen = {}
        for word in words:
            word += '#'
            if word in seen:
                indices.append(seen[word])
            else:
                for i in range(len(word)-1):
                    seen[word[i:]] = i + len(res) # note this step is O(k**2) bcos creating one substring is O(k), and we need to create k substrings
                indices.append(len(res))
                res += word
            # print(res, word, seen)
                
        return len(res)
        
class Solution_trie: # code is a bit hard to understand
    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        # emit, em, lleb
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)