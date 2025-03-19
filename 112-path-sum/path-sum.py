# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node , num):
            if not node:
                return False
            
            num += node.val
            if not node.left and not node.right:
                return num == targetSum
            
            return helper(node.left, num) or helper(node.right, num)
            
        return helper(root, 0)
