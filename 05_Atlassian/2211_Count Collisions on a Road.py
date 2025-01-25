class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        stack = []

        for car in directions:
            if car == 'L':
                if not stack:
                    continue
                if stack[-1] == 'S':
                    res += 1
                if stack[-1] == 'R':
                    res += 2
                    stack.pop()
                    while stack and stack[-1] == 'R':
                        res += 1
                        stack.pop()
                    stack.append('S')
            
            if car == 'S':
                while stack and stack[-1] == 'R':
                    res += 1
                    stack.pop()
                stack.append('S')
            
            if car == 'R':
                stack.append('R')
        
        return res