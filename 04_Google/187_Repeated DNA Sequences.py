class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        n = len(s)
        res = set()

        for i in range(n - 9):
            temp = s[i : i + 10]
            if temp in seen:
                res.add(temp)
            else:
                seen.add(temp)
        
        return list(res)