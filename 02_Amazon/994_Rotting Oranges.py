class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        fresh, rotten = set(), deque()
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    rotten.append((i, j))
        
        if len(fresh) == 0:
            return 0
        
        if len(rotten) == 0:
            return -1
    
        while rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for dx, dy in DIRS:
                    nx, ny = i + dx, j + dy
                    if (nx, ny) in fresh:
                        fresh.remove((nx, ny))
                        rotten.append((nx, ny))
            res += 1
        
        return res - 1 if len(fresh) == 0 else -1