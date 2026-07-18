# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = deque([[root,root.val]])
        count = 0

        while queue:
            for _ in range(len(queue)):
                node, curr_max = queue.popleft()

                if node.val >= curr_max:
                    curr_max = node.val
                    count += 1
                
                if node.left:
                    queue.append([node.left, curr_max])
                if node.right:
                    queue.append([node.right, curr_max])

        return count

