# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)

            i = inorder_idx[val]
            root.left = helper(left, i - 1)
            root.right = helper(i + 1, right)
            return root
        
        return helper(0, len(inorder) - 1)