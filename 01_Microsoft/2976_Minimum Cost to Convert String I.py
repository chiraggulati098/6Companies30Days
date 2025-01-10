class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf')] * 26 for _ in range(26)]

        for i in range(len(original)):
            dist[ord(original[i]) - 97][ord(changed[i]) - 97] = min(cost[i], dist[ord(original[i]) - 97][ord(changed[i]) - 97])
        
        for i in range(26):
            dist[i][i] = 0
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        res = 0
        for i in range(len(source)):
            if dist[ord(source[i]) - 97][ord(target[i]) - 97] == float('inf'):
                return -1
            res += dist[ord(source[i]) - 97][ord(target[i]) - 97] 
        
        return res