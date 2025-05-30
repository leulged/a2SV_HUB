# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
                root = TreeNode(val)
                return root
        def insert(node):
        
            if not node.left:
                if val < node.val:
                    node.left = TreeNode(val)
                    return node

            if not node.right:
                if val > node.val:
                    node.right = TreeNode(val)
                    return node

            if val > node.val:
                return insert(node.right)
            
            if val < node.val:
                return insert(node.left)

        insert(root)
        return root