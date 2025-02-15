class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0 or (r, c) in visit
            ):
                return
            visit.add((r, c))
            NEI = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for x, y in NEI:
                dfs(x, y, visit)
        
        def count_islands():
            visit = set()
            cnt = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] and (r, c) not in visit:
                        dfs(r, c, visit)
                        cnt += 1
            
            return cnt
        
        if count_islands() != 1:
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                if count_islands() != 1:
                    return 1
                grid[r][c] = 1
        
        return 2