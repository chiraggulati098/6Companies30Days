class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n, n1, n2 = len(s), len(a), len(b)
        res = []
        a_starts, b_starts = [], []

        for i in range(n - n1 + 1):
            if a == s[i : i + n1]:
                a_starts.append(i)
            
        for i in range(n - n2 + 1):
            if b == s[i : i + n2]:
                b_starts.append(i)
        
        for i in a_starts:
            for j in b_starts:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        
        return res