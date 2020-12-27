class Solution_slow:
    def decodeAtIndex(self, S: str, K: int) -> str:
        result = ""
        idx = 0
        while idx < len(S) and len(result) < K:
            this_char =  S[idx]
            if not this_char.isdigit():
                result += this_char
            else:
                result *= int(this_char)
            idx += 1

        return result[K-1]

# this is too slow
# abc23b4, K = 20
# ((abcabc)(abcabc)(abcabc)b)((abcabc)(abcabc)(abcabc)b)((abcabc)(abcabc)(abcabc)b)((abcabc)(abcabc)(abcabc)b)

class Solution_fast:
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1
