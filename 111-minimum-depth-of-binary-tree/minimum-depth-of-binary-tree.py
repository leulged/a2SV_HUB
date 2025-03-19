# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node , depth , minimum):
            if not node:
                return float("inf")

            if not node.left and not node.right:
                return depth

            left_minimum = min(minimum , helper(node.left , depth + 1, minimum))
            right_minimum = min(minimum , helper(node.right , depth + 1 , minimum))

            return min(left_minimum , right_minimum)

        if not root:
            return 0
            
        return helper(root , 1, float("inf"))