# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        mx = 0
        
        def dfs(node, mv):
            nonlocal mx
            
            if not node:
                return 
                
            mx = max(mx, mv)

            if node.left:
                dfs(node.left, mv + 1)

            if node.right:
                dfs(node.right, mv + 1)

        dfs(root, 1)

        return mx