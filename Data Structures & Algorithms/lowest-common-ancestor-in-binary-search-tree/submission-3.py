# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        if p.val > q.val:
            p, q = q, p

        while node.val < p.val or q.val < node.val:
            if node.val < p.val:
                node = node.right
            else:
                node = node.left

        return node