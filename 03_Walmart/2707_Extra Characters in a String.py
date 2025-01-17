class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 0
            
            # skip cur element
            res = 1 + helper(i + 1)

            for j in range(i, len(s)):
                if s[i : j + 1] in words:
                    res = min(res, helper(j + 1))
            
            memo[i] = res
            return memo[i]
        
        return helper(0)