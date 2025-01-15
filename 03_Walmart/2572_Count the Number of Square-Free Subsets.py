class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        sq = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        cnt = {}
        for i in nums:
            if i in sq:
                continue
            temp = dict(cnt)
            for k in cnt.keys():
                if gcd(k, i) == 1:
                    cur = k * i
                    if cur in temp:
                        temp[cur] += cnt[k]
                    else:
                        temp[cur] = cnt[k]
            
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
            cnt = temp
        
        return sum([cnt[k] for k in cnt.keys()]) % (10 ** 9 + 7)