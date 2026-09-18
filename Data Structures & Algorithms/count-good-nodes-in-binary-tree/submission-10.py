# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxsofar):
            if not root:
                return 0

            if root.val >= maxsofar:
                count = 1
            else:
                count = 0
                
            maxsofar = max(maxsofar, root.val)

            count += dfs(root.left, maxsofar)
            count += dfs(root.right, maxsofar)

            return count

        return dfs(root, root.val)
        
