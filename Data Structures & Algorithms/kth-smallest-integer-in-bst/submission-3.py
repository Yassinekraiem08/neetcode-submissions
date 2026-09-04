# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []

        def ksmallest(root):
            if not root:
                return 0
            
            ksmallest(root.left)
            output.append(root.val)
            ksmallest(root.right)
        
        ksmallest(root)
        
        return output[k-1]
