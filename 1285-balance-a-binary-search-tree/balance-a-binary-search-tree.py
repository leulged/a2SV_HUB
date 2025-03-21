# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ls = []
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            ls.append(node.val)
            inorder(node.right)
        inorder(root)

        print(ls)
        def balance(ls):
            if not ls:
                return None
            
            mid = len(ls) // 2
            node = TreeNode(ls[mid])

            node.left = balance(ls[:mid])
            node.right = balance(ls[mid + 1:])
            
            return node
        
        return balance(ls)
            