# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = [root]
        mp = {None : 0 } #height, diameter

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                height = max(mp[node.left], mp[node.right]) + 1
                res = max(res, mp[node.left] + mp[node.right])
                mp[node] = height
                stack.pop()
        
        return res