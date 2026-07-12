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
        
        return self.flip(root)
    
    def flip(self, node):
        left = node.left if node.left else None
        right = node.right if node.right else None
        
        node.left = self.flip(right) if right else None
        node.right = self.flip(left) if left else None

        return node