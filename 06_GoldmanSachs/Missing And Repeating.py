#User function Template for python3
from collections import defaultdict

class Solution:
    def findTwoElement( self,arr): 
        # code here
        freq = defaultdict(int)
        repeating = -1
        missing = -1
        
        for x in arr:
            freq[x] += 1
            if freq[x] == 2:
                repeating = x
        
        s = set(arr)
        for i in range(1, len(arr) + 1) :
            if i not in s:
                missing = i
        
        return [repeating, missing]

