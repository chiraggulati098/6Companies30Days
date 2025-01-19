class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        arr = [x[1] for x in env]
        
        def LIS(arr):
            n = len(arr)
            lis = [arr.pop(0)]

            # bisect left implementation
            def get_idx(arr, num):
                l, r = 0, len(arr)
                while l < r:
                    m = (l + r) // 2
                    if arr[m] == num:
                        return m
                    elif arr[m] > num:
                        r = m
                    else:
                        l = m + 1
                    
                return l

            for num in arr:
                if num > lis[-1]:
                    lis.append(num)
                else:
                    lis[get_idx(lis, num)] = num
            
            return len(lis)
        
        return LIS(arr)