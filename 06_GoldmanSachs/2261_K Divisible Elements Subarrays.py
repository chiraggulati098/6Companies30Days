class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        n = len(nums)

        for left in range(n):
            temp = []
            count = 0

            for right in range(left, n):
                if nums[right] % p == 0:
                    count += 1
                
                temp.append(nums[right])
                if count > k:
                    break
                
                res.add(tuple(temp))
        
        return len(res)