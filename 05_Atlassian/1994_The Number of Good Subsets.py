class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        count = defaultdict(int)
        MOD = 10 ** 9 + 7

        for num in nums:
            count[num] += 1
        
        dp = [1] + [0] * (1 << 10)

        for a in count:
            if a == 1:
                continue
            
            if a % 4 == 0 or a % 9 == 0 or a == 25:
                continue
            
            mask = sum(1 << i for i, p in enumerate(P) if a % p == 0)
            for i in range(1 << 10):
                if i & mask:
                    continue
                dp[i | mask] = (dp[i | mask] + count[a] * dp[i]) % MOD
        
        return (1 << count[1]) * (sum(dp) - 1) % MOD