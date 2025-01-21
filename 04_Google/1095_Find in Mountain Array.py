# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # find peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        
        # binary search left
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if mountainArr.get(m) < target:
                l = m + 1
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                return m

        # binary search right
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            if mountainArr.get(m) > target:
                l = m + 1
            elif mountainArr.get(m) < target:
                r = m - 1
            else:
                return m
        
        return -1