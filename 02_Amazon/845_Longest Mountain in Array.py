class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 0
        res = 0
        n = len(arr)

        # simulate walking on the mountain
        while i < n:
            base = i

            while i + 1 < n and arr[i + 1] > arr[i]:
                i += 1
            
            # check if moved from base
            if i == base:
                i += 1
                continue
            
            peak = i

            while i + 1 < n and arr[i + 1] < arr[i]:
                i += 1
            
            # check if moved from peak
            if i == peak:
                i += 1
                continue
            
            res = max(res, i - base + 1)
    
        return res