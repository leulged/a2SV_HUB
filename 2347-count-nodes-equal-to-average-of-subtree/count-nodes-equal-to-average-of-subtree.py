# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def helper(node):
            nonlocal count
            if not node :
                return (0 , 0)
            
            left_sum , left_count = helper(node.left)
            right_sum , right_count = helper(node.right)

            total = left_sum + right_sum + node.val
            total_cnt = left_count + right_count + 1
            
            average = total // total_cnt 

            if average == node.val:
                count += 1
            
            return (total , total_cnt)
            
        helper(root)

        return count