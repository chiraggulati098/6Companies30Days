class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        total = sum(nums)
        cur = sum(i * nums[i] for i in range(n))
        res = cur

        for i in range(1, n):
            cur += total - n * nums[n - i]
            res = max(res, cur)
        
        return res