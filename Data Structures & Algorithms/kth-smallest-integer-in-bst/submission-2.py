# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        remaining = k

        while curr:
            if not curr.left:
                remaining -= 1
                if remaining == 0:
                    return curr.val
                else:
                    curr = curr.right
            else:
                pred = curr.left
                # find inorder predecessor (rightmost node in left subtree)
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    remaining -= 1
                    if remaining == 0:
                        return curr.val
                    curr = curr.right
