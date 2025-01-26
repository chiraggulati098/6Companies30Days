class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        l, r = 1, 2 * 10 ** 9
        ans = r
        lcm = (divisor1 * divisor2) // gcd(divisor1, divisor2)

        while l <= r:
            m = (l + r) // 2
            x = m - m // divisor1
            y = m - m // divisor2
            z = m - m // lcm

            if x < uniqueCnt1 or y < uniqueCnt2 or z < (uniqueCnt1 + uniqueCnt2):
                l = m + 1
            else:
                ans = min(ans, m)
                r = m - 1
        
        return ans