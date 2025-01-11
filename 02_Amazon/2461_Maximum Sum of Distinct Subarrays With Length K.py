class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        freq = defaultdict(int)

        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            cur += nums[r]

            if r - l + 1 > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    freq.pop(nums[l])
                cur -= nums[l]
                l += 1
            
            if len(freq) == r - l + 1 == k:
                res = max(res, cur)
            
        return res