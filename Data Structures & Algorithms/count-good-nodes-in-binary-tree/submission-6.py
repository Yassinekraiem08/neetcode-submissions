# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxvalue: int):
            if not root:
                return 0

            if root.val >= maxvalue:
                count = 1
            else:
                count = 0

            new_max = max(maxvalue, root.val)

            count += helper(root.left, new_max)
            count += helper(root.right, new_max)

            return count
        
        return helper(root, root.val)