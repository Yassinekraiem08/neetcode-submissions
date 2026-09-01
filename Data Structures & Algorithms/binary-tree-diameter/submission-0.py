# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = 0
        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
        
            height_left = dfs(root.left)
            height_right = dfs(root.right)

            self.result = max(self.result, height_left + height_right)
            return 1 + max(height_left, height_right)
            
        dfs(root)
        return self.result