"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen = {}
        def dfs(curr):
            if curr.val not in seen:
                seen[curr.val] = Node(curr.val)
                seen[curr.val].neighbors = [
                    dfs(neighbor)
                    for neighbor in curr.neighbors
                ]
            return seen[curr.val]
        
        return dfs(node)
