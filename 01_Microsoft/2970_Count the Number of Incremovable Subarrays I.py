class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            arr = nums.copy()
            for j in range(n - i):
                arr.pop(i)
                if arr == sorted(set(arr)):
                    res += 1
        
        return res