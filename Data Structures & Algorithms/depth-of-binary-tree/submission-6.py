# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([[root, 1]])
        res = 1

        while queue:
            node, depth = queue.popleft()

            if node:
               res = max(res, depth)
               queue.append([node.left, depth + 1])
               queue.append([node.right, depth + 1]) 

        return res