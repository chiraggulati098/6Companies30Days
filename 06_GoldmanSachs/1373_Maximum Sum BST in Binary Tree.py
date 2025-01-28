# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(root):
            if not root:
                return (0, float('inf'), float('-inf'))

            a, amin, amax = helper(root.left) if root.left else (0, float('inf'), float('-inf'))
            b, bmin, bmax = helper(root.right) if root.right else (0, float('inf'), float('-inf'))

            if a is not None and b is not None:
                if amax < root.val < bmin:
                    s = root.val + a + b
                    self.res = max(self.res, s)
                    return s, min(root.val, amin), max(root.val, bmax)
            
            return (None, None, None)
        
        helper(root)
        return self.res