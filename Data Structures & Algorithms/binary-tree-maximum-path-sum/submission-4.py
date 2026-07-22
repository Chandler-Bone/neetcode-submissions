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
            
            left = dfs(node.left)
            right = dfs(node.right)

            biggest_side = max(left, right)

            node_max = max(node.val, biggest_side + node.val)
            self.tree_max = max(self.tree_max, left + right + node.val)
            self.tree_max = max(self.tree_max, node_max)

            return node_max

        dfs(root)
        return self.tree_max