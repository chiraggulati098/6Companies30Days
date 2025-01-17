class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    q = deque([(i, j)])
                    board[i][j] = '-'

                    while q:
                        x, y = q.popleft()
                        for dx, dy in DIRS:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                                if board[nx][ny] == 'X':
                                    q.append((nx, ny))
                                    board[nx][ny] = '-'
                    
                    res += 1
        
        return res