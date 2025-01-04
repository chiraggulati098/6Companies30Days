class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()

        m = (n - 1) // 2
        nums[:: 2], nums[1 :: 2] = nums[m :: -1], nums[: m : -1]