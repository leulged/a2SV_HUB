# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(lambda : float("-inf"))
        
        def find(node, level):
            if not node:
                return 
            
            ans[level] = max(node.val, ans[level])
            find(node.left , level + 1)
            find(node.right , level + 1)

        find(root, 0)
        print(ans)
        ls = [i for i in ans.values()]

        return ls


        



        