class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == "":
            return []
        
        mappings = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        res = mappings[digits[0]]

        def helper(digit):
            ans = []

            for i in res:
                for j in mappings[digit]:
                    ans.append(i + j)

            return ans
        
        for i in range(1, len(digits)):
            res = helper(digits[i])
        
        return res