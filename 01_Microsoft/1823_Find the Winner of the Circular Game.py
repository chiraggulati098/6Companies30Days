class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x for x in range(1, n + 1)]
        idx = 0

        while len(arr) != 1:
            removeIdx = (idx + k - 1) % len(arr)
            arr.pop(removeIdx)
            idx = removeIdx
        
        return arr[0]