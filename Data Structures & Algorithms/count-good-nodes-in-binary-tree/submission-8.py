# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, bestsofar):
            if not root:
                return 0

            if root.val >= bestsofar:
                count = 1
            else:
                count = 0
            
            bestsofar = max(bestsofar, root.val)

            count += dfs(root.left, bestsofar)
            count += dfs(root.right, bestsofar)

            return count
    
        return dfs(root, root.val)