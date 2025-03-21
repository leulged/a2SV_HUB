# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        minimum = ''
        st = "abcdefghijklmnopqrstuvwxyz"
        def small(node , path):
            nonlocal minimum
            nonlocal st
            if not node:
                return 
            
            path += st[node.val]
            if not node.left and not node.right:
                print(1)
                if not minimum:
                    minimum = path[::-1]
                
                else:
                    if minimum > path[::-1]:
                        minimum = path[::-1]
            
            small(node.left , path)
            small(node.right , path)

        small(root , "")
        return minimum
