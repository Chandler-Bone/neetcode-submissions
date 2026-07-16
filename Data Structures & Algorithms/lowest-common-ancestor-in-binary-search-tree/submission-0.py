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

        print(node.val)
        print(p.val)
        print(q.val)

        while p.val > node.val or node.val > q.val:
            if p.val > node.val:
                node = node.right
            else:
                node = node.left

        return node
            