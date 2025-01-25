class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = len(arr1)

        for x in arr1:
            for y in arr2:
                if abs(x - y) <= d:
                    res -= 1
                    break
        
        return res