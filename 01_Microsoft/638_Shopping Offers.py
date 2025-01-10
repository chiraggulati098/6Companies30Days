class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)
        memo = {}

        def helper(needed):
            for need in needed:
                if need < 0:
                    return float("inf")
            
            if tuple(needed) in memo:
                return memo[tuple(needed)]
            
            min_val = 0
            for i in range(n):
                min_val += price[i] * needed[i]
            
            for s in special:
                new_needed = needed.copy()
                for i in range(len(s) - 1):
                    new_needed[i] -= s[i]
                min_val = min(min_val, s[-1] + helper(new_needed))
            
            memo[tuple(needed)] = min_val
            return memo[tuple(needed)]
        
        return helper(needs)