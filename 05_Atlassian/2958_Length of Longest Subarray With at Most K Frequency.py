class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        freq = defaultdict(int)
        
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1

            if freq[nums[r]] > k:
                while freq[nums[r]] > k:
                    freq[nums[l]] -= 1
                    l += 1
            
            res = max(res, r - l + 1)
        
        return res