class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        memo = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        res = 0

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
                    res = max(res, memo[i][j])
        
        return res