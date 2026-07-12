# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = root.left if root.left else None
        right = root.right if root.right else None
        
        root.left = self.invertTree(right) if right else None
        root.right = self.invertTree(left) if left else None

        return root
    
