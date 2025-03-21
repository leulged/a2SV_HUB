# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def helper(node , path):
            nonlocal ans
            
            if not node:
                return 

            path += str(node.val)
            
            if not node.left and not node.right:
                return ans.append(path)

            
            helper(node.left, path + "->" )
            helper(node.right , path + "->" )

        helper(root , "")

        return ans
            
