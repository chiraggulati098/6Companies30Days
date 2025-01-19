class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)

        for _ in range(k):
            heappush(nums, heappop(nums) + 1)
        
        res = 1
        for x in nums:
            res = (res * x) % (10 ** 9 + 7)
        
        return res 