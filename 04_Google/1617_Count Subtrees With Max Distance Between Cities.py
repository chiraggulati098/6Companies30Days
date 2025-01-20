from itertools import combinations, permutations

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[999 for _ in range(n)] for _ in range(n)]

        for [i, j] in edges:
            graph[i - 1][j - 1] = 1
            graph[j - 1][i - 1] = 1
        
        for k, i, j in permutations(range(n), 3):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        res = [0] * (n - 1)
        for k in range(2, n + 1):
            for s in combinations(range(n), k):
                e = sum(graph[i][j] for i, j in combinations(s, 2) if graph[i][j] == 1)
                d = max(graph[i][j] for i, j in combinations(s, 2))
                if e == k - 1:
                    res[d - 1] += 1
        
        return res