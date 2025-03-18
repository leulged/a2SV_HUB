"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return []

        ans.append(root.val)
          
        for child in root.children:
            
            ans.extend(self.preorder(child))    
        
        return ans