class Solution:
    def asteroidsDestroyed(self, mass: int, arr: List[int]) -> bool:
        arr.sort()
        
        for a in arr:
            if a > mass:
                return False
            
            mass += a
        
        return True