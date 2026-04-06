# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
            else:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return ",".join(map(str, res))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = []
        items = data.split(",")
        self.idx = 0

        def dfs():
            curr = self.idx
            self.idx += 1
            if items[curr] == "N":
                return None
            else:
                node = TreeNode(int(items[curr]))
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs()
