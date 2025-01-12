class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        res = []

        for i in range(len(s)):
            res_str = set()
            for x in contact:
                if x.startswith(s[: i + 1]):
                    res_str.add(x)
            if len(res_str) != 0:
                res.append(sorted(res_str))
            else:
                res.append('0')
        
        return res