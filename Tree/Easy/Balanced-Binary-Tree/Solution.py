# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        Flag = True
        def height(root):
            nonlocal Flag
            if root == None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if abs(lh-rh) > 1:
                    Flag = False
                    return max(lh,rh) + 1
            return max(lh,rh) + 1
        height(root)
        return Flag
        