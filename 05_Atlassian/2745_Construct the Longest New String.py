class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return 2 * (min(x, y) * 2 + z)
        return 2 * (min(x, y) * 2 + 1 + z)