class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        stack = [arr[0]]
        n = len(arr)

        if arr[0] == '#':
            return n == 1
        
        for i in range(1, n):
            if arr[i] != '#':
                stack.append(arr[i])
            else:
                if not stack:
                    return i == n - 1
                stack.pop()

        return False