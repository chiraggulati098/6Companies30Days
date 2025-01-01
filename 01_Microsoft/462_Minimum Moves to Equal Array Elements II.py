class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        midNum = nums[len(nums) // 2]

        res = 0
        for num in nums:
            res += abs(midNum - num)
        
        return res