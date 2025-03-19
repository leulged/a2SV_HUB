# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def find(node):
            nonlocal count
            if not node:
                return []
            
            count[node.val] += 1
            find(node.left)
            find(node.right)

        find(root)
        maximum = max(count.values()) 

        ans = []
        for key , val in count.items():
            if val == maximum:
                ans.append(key)
        
        return ans
        
  