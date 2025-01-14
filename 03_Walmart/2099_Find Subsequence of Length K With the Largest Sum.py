class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)

        selected = sorted(nums, reverse = True)
        selected = selected[: k]
        freq = defaultdict(int)

        for num in selected:
            freq[num] += 1

        for i in range(n):
            if freq[nums[i]] > 0:
                res.append(nums[i])
                freq[nums[i]] -= 1
        
        return res