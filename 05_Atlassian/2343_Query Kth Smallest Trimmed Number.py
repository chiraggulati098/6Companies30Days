class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums[0])
        res = []

        for query in queries:
            k, trim = query

            heap = []
            for i, num in enumerate(nums):
                heappush(heap, (int(num[n - trim :]), i))
            
            for _ in range(k - 1):
                heappop(heap)
            
            num, i = heappop(heap)
            res.append(i)
        
        return res