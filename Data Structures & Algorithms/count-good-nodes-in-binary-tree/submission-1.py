# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, curr_max):
            if not node:
                return 0
            
            res = 0

            if curr_max <= node.val:
                res += 1
                curr_max = node.val

            res += dfs(node.left, curr_max)
            res += dfs(node.right, curr_max)

            return res

        return dfs(root, root.val)