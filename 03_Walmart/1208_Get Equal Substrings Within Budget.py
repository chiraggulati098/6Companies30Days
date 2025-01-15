class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = []
        n = len(s)

        for i in range(n):
            cost.append(abs(ord(s[i]) - ord(t[i])))
        
        res = cur = l = 0
        for r in range(n):
            cur += cost[r]

            while cur > maxCost and l <= r:
                cur -= cost[l]
                l += 1
            
            if cur <= maxCost:
                res = max(res, r - l + 1)
            
        return res