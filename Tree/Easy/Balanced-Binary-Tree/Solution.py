# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            
            lh = height(node.left)
            if lh == -1:
                return -1  # left already unbalanced, bail out immediately
            
            rh = height(node.right)
            if rh == -1:
                return -1  # right already unbalanced, bail out immediately
            
            if abs(lh - rh) > 1:
                return -1  # this node itself is unbalanced
            
            return max(lh, rh) + 1
        
        return height(root) != -1