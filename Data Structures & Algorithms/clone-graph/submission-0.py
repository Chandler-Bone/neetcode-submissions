"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        queue = deque([node])

        while queue:
            curr = queue.popleft()
            
            oldToNew[curr] = Node(curr.val)

            for n in curr.neighbors:
                if n not in oldToNew:
                    queue.append(n)

        for i in oldToNew:
            for n in i.neighbors:
                oldToNew[i].neighbors.append(oldToNew[n])

        return oldToNew[node]

        
        