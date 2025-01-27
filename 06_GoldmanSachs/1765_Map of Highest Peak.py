class Solution:
    def highestPeak(self, arr: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(arr), len(arr[0])
        q = deque([])
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if arr[r][c] == 1:
                    arr[r][c] = 0
                    q.append((r, c))
                else:
                    arr[r][c] = -1
        
        while q:
            r, c = q.popleft()
            for x, y in DIRS:
                nr, nc = r + x, c + y
                if (
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    arr[nr][nc] == -1
                ):

                    arr[nr][nc] = arr[r][c] + 1
                    q.append((nr, nc))
        
        return arr