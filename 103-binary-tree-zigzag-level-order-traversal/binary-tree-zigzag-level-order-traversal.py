# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dict = defaultdict(list)
        def zigzagfind(node , level):
            if not node:
                return 
            
            my_dict[level].append(node.val)
            zigzagfind(node.left , level + 1)
            zigzagfind(node.right , level + 1)
      
        zigzagfind(root, 0)
        result = []

        for level in sorted(my_dict.keys()):  
            if level % 2 == 1:
                result.append(my_dict[level][::-1])  
            else:
                result.append(my_dict[level])

        return result
        
            
        