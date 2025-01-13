class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        num = columnNumber

        while num:
            res = chr(ord('A') + (num - 1) % 26) + res
            num = (num - 1) // 26
        
        return res