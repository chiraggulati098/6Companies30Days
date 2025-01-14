# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(dict)
        
        def create_graph(cur):
            if cur.left:
                graph[cur.val][cur.left.val] = 1
                graph[cur.left.val][cur.val] = 1
                create_graph(cur.left)
            if cur.right:
                graph[cur.val][cur.right.val] = 1
                graph[cur.right.val][cur.val] = 1
                create_graph(cur.right)
        
        create_graph(root)

        def djikstra():
            dist = {node: float("inf") for node in graph}
            dist[start] = 0

            pq = [(0, start)]
            heapq.heapify(pq)

            visited = set()

            while pq:
                cur_dist, cur_node = heapq.heappop(pq)
                if cur_node in visited:
                    continue
                
                visited.add(cur_node)
                for nei, wei in graph[cur_node].items():
                    new_dist = wei + cur_dist
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(pq, (dist[nei], nei))
            
            return dist
        
        dist = djikstra()
        
        res = 0
        for i in dist:
            res = max(res, dist[i])
        
        return res