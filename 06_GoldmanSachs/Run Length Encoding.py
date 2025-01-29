
class Solution:
    def encode(self, s : str) -> str:
        # code here
        if not s:
            return ''
        
        res = s[0]
        
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == res[-1]:
                cnt += 1
            else:
                res += str(cnt) + s[i]
                cnt = 1
        
        res += str(cnt)
        return res