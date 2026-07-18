# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            for _ in range(len(queue)):
                node, curr_min, curr_max = queue.popleft()

                if not curr_min < node.val < curr_max:
                    return False

                if node.left:
                    queue.append((node.left, curr_min, min(curr_max, node.val)))
                if node.right:
                    queue.append((node.right, max(curr_min, node.val), curr_max))

        return True