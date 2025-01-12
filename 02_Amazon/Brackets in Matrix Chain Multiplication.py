class Solution:
    def matrixChainOrder(self, arr):
        # code here
        n = len(arr)
        memo = {}
        
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
                
            if i == j:
                temp = chr(ord('A') + i)
                memo[(i, j)] = (temp, 0)
                return memo[(i, j)]
            
            res = float("inf")
            s = ''
            
            for k in range(i + 1,  j + 1):
                left = helper(i, k - 1)
                right = helper(k, j)
                
                cur = left[1] + right[1] + arr[i] * arr[k] * arr[j + 1]
                
                if res > cur:
                    res = cur
                    s = "(" + left[0] + right[0] + ")"
                
            memo[(i, j)] = (s, res)
            return memo[(i, j)]
    
        return helper(0, n - 2)[0]