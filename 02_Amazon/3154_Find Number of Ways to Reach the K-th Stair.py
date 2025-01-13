class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        memo = {}

        def helper(cur, jump, up):
            if (cur, jump, up) in memo:
                return memo[(cur, jump, up)]

            # passed k and can never come back
            if cur > k + 1:
                return 0
            
            res = 0
            # if at k
            if cur == k:
                res += 1
            
            # go up
            res += helper(cur + (2 ** jump), jump + 1, True)
            # go down if didn't go down till now
            if up and cur > 0:
                res += helper(cur - 1, jump, False)
            
            memo[(cur, jump, up)] = res
            return memo[(cur, jump, up)]
        
        return helper(1, 0, True)