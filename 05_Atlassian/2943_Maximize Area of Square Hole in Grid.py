class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxH, maxV, temp = 1, 1, 1

        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                temp += 1
            else:
                temp = 1
            maxH = max(maxH, temp)
        
        temp = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                temp += 1
            else:
                temp = 1
            maxV = max(maxV, temp)        
        
        sq_side = min(maxH + 1, maxV + 1)
        return sq_side ** 2