"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(curr):
            if curr in clones:
                return clones[curr]
            else:
                cloned = Node(curr.val)
                clones[curr] = cloned
                for neighbor in curr.neighbors:
                    cloned.neighbors.append(dfs(neighbor))
                return cloned
        
        return dfs(node) if node else None
