# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        sentinel = curr = TreeNode()
        i = j = 0
        while i < len(preorder) and j < len(inorder):
            curr.right = TreeNode(preorder[i], right=curr.right)
            curr = curr.right
            
            i += 1
            while i < len(preorder) and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            
            j += 1
            while j < len(inorder) and curr.right and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return sentinel.right
