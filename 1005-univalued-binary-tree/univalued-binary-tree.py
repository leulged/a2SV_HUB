# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        x = root.val
        while queue:
            curr = queue.popleft()
            if curr.left :
                queue.append(curr.left)
            if curr.right :
                queue.append(curr.right)

            if curr.val != x:
                return False
            
        return True