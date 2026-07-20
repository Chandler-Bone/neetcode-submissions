# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.tree_max = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            node_max = node.val
            left = dfs(node.left)
            right = dfs(node.right)

            path_max = max(left, right)
            node_max = max(node_max, path_max + node.val)

            self.tree_max = max(self.tree_max, node_max)
            self.tree_max = max(self.tree_max, left + node.val + right)

            return node_max

        dfs(root)
        return self.tree_max
