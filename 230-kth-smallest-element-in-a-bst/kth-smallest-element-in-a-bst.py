# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0
        def helper(node, k):
            nonlocal count
            nonlocal result
            if not node:
                return 

            
            
            helper(node.left , k )
            count += 1
            if count == k:
                result =  node.val

            helper(node.right , k)
        
        helper(root, k)
        return result