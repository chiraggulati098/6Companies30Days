class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])

        def avg_value(r, c):
            total, cnt = 0, 0

            up = max(0, r - 1)
            down = min(ROWS - 1, r + 1)
            left = max(0, c - 1)
            right = min(COLS - 1, c + 1)

            for row in range(up, down + 1):
                for col in range(left, right + 1):
                    total += img[row][col]
                    cnt += 1
            
            return total // cnt
        
        return [[avg_value(r, c) for c in range(COLS)] for r in range(ROWS)]