class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)
        
        visited = set()
        def dfs(prev, curr):
            if curr in visited:
                return False
            else:
                visited.add(curr)
                for node in adj[curr]:
                    if node == prev:
                        continue
                    if not dfs(curr, node):
                        return False
                return True
        
        return dfs(-1, 0) and len(visited) == n
