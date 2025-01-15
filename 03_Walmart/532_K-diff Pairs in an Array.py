class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        if k == 0:
            for num, cnt in freq.items():
                if cnt > 1:
                    res += 1
        else:
            for num, cnt in freq.items():
                if num + k in freq:
                    res += 1

        return res