# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0

        def dfs(node, cur_max):
            if not node:
                return None

            if node.val >= cur_max:
                self.count += 1
                cur_max = node.val

            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
        dfs(root, root.val)

        return self.count