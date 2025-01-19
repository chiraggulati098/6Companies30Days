class Solution:
    def stoneGameVI(self, arrA: List[int], arrB: List[int]) -> int:
        n = len(arrA)
        arr = [None] * n

        for i in range(n):
            arr[i] = (arrA[i], arrB[i])
        
        arr.sort(key = lambda x: sum(x), reverse = True)

        a = sum([i[0] for i in arr[::2]])
        b = sum([i[1] for i in arr[1::2]])
        
        if a > b:
            return 1
        elif b > a:
            return -1
        else:
            return 0