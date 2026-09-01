# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def good(root: TreeNode, maxvalue: int)-> int:
            if not root:
                return 0
                
            if root.val >= maxvalue:
                count = 1 
            else:
                count = 0

            new_max = max(maxvalue, root.val)

            if root.right:
                count += good(root.right, new_max)
            if root.left:
                count += good(root.left, new_max)
        
            return count
    
        return good(root, root.val)