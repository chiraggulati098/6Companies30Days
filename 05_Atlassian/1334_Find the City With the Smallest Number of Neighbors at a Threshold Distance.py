class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        # set distance from edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # use Floyd-Warshall algo to find shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_count = n
        result_city = 0

        for i in range(n):
            reachable_cities = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachable_cities += 1
            
            if reachable_cities <= min_count:
                min_count = reachable_cities
                result_city = i
        
        return result_city