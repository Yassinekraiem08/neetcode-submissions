# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def ksmallest (root: Optional[TreeNode]):
            if not root:
                return

            ksmallest(root.left)
            res.append(root.val)
            ksmallest(root.right)

        ksmallest(root)
        
        return res[k-1]