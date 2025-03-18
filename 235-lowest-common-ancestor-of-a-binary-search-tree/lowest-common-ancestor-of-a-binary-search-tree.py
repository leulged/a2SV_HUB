# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor_finder(node , p , q):
            if not node:
                return None
            
            if node == p or node == q:
                return node

            if p.val < node.val < q.val or q.val < node.val < p.val:
                return node
            
            if p.val < node.val and q.val < node.val:
                return ancestor_finder(node.left , p , q)
            
            if p.val > node.val and q.val > node.val:
                return ancestor_finder(node.right , p , q)

        return ancestor_finder(root , p , q)

            
