# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        queue = deque([root])
        res = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node:
                    res.append("N")
                else:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "N":
            return None

        nodes = data.split(",")
        
        root = TreeNode(nodes[0])
        queue = deque([root])
        count = 1

        while queue:
            node = queue.popleft()

            if nodes[count] != "N":
                node.left = TreeNode(nodes[count])
                queue.append(node.left)
            count += 1
            if nodes[count] != "N":
                node.right = TreeNode(nodes[count])
                queue.append(node.right)
            count += 1
            
        return root