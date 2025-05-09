"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        max_child_depth = 0

        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth > max_child_depth:
                max_child_depth = child_depth
        
        return max_child_depth + 1