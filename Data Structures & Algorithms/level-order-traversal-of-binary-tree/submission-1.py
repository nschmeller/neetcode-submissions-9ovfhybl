# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            curr, level = q.popleft()
            res[level].append(curr.val)
            if curr.left:
                q.append((curr.left, level+1))
            if curr.right:
                q.append((curr.right, level+1))
        
        return [res[i] for i in range(len(res))]
