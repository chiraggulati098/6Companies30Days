class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects        
        self.weight = []
        for a, b, x, y in self.rects:
            self.weight.append((y - b + 1) * (x - a + 1))
        self.total = sum(self.weight)
        
        for i in range(1, len(self.weight)):
            self.weight[i] += self.weight[i - 1]
        self.weight = [0] + self.weight

    def pick(self) -> List[int]:
        
        # bisect left implementation
        def get_idx(arr, num):
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] == num:
                    return m
                elif arr[m] > num:
                    r = m
                else:
                    l = m + 1
            
            return l

        idx = get_idx(self.weight, random.randint(1, self.total))
        a, b, x, y = self.rects[idx - 1]
        return [random.randint(a, x), random.randint(b, y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()