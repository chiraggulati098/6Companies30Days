class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = 1 if nums[i] % 2 != 0 else 0
        
        odd_count, res = 0, 0
        
        # 3 pointer approach
        l, m = 0, 0
        for r in range(n):
            if nums[r]:
                odd_count += 1
            
            while odd_count > k:
                odd_count -= 1 if nums[l] == 1 else 0
                l += 1
            m = l
            
            if odd_count == k:
                while nums[m] != 1:
                    m += 1
                res += (m - l) + 1
        
        return res