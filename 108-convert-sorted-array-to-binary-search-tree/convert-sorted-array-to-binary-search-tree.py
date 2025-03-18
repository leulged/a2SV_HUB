# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:  
            return None

        mid = len(nums) // 2
        node = TreeNode(nums[mid])  
        
        def bst(node, left, right):
            if left:
                mid_l = len(left) // 2
                node.left = TreeNode(left[mid_l])  
                bst(node.left, left[:mid_l], left[mid_l+1:])  
            
            if right:
                mid_r = len(right) // 2
                node.right = TreeNode(right[mid_r])  
                bst(node.right, right[:mid_r], right[mid_r+1:])  

        bst(node, nums[:mid], nums[mid + 1:])
        return node