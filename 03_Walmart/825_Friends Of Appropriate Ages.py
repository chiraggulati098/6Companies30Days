class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0

        freq = defaultdict(int)
        for age in ages:
            freq[age] += 1
        
        for x in freq:
            x_count = freq[x]

            for y in freq:
                if not (y <= 0.5 * x + 7 or age > me):
                    if y != x:
                        res += freq[y] * x_count
                    else:
                        res += int(x_count * (x_count - 1))
        
        return res