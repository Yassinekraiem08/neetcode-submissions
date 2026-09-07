# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def canreachleaf(root, pathsum):
            if not root:
                return False
            pathsum += root.val

            if not root.left and not root.right:
                return pathsum == targetSum
            
            if canreachleaf(root.left, pathsum):
                return True
            
            if canreachleaf(root.right, pathsum):
                return True

            return False

        return canreachleaf(root, 0)