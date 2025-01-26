class Solution:

    def __init__(self, m: int, n: int):
        self.N = m * n - 1
        self.ROWS = m
        self.COLS = n
        self.flipped = set()

    def flip(self) -> List[int]:
        temp = random.randint(0, self.N)
        while temp in self.flipped:
            temp = random.randint(0, self.N)
        
        self.flipped.add(temp)
        return [temp // self.COLS, temp % self.COLS]

    def reset(self) -> None:
        self.flipped = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()