class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        p = {}      # dict to store mask and length

        for mask in range(1, 1 << n):       # create all subsequences
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            
            if subseq == subseq[::-1]:      # check if palindrome
                p[mask] = len(subseq)

        res = 0
        for m1 in p:
            for m2 in p:
                if m1 & m2 == 0:            # check if disjoint
                    res = max(res, p[m1] * p[m2])
        
        return res