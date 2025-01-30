class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}
        def helper(pos, steps):
            if (pos, steps) in memo:
                return memo[(pos, steps)]

            if steps == k:
                memo[(pos, steps)] = 1 if pos == endPos else 0
                return memo[(pos, steps)]
            
            memo[(pos, steps)] = helper(pos + 1, steps + 1) + helper(pos - 1, steps + 1)
            return memo[(pos, steps)]
        
        return helper(startPos, 0) % MOD