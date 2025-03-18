# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def max_diff_finder(node , maximum , minimum):
            curr = 0
            if not node:
                return maximum - minimum 
            
            maximum = max(maximum , node.val)
            
            minimum = min(minimum , node.val)
            
            left_diff = max_diff_finder(node.left, maximum, minimum)

            right_diff = max_diff_finder(node.right, maximum, minimum)
            
            return max(left_diff, right_diff) 
            
        return max_diff_finder(root , root.val , root.val)

            

            