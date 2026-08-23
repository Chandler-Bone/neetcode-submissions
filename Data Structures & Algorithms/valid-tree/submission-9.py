class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_map = { i:[] for i in range(n)}

        for node, cnode in edges:
            adj_map[node].append(cnode)
            adj_map[cnode].append(node)

        cycle = set()
        self.visited = 0
        def dfs(node, pnode):
            self.visited += 1
            if node in cycle:
                return False
            if adj_map[node] == []:
                return True
            
            cycle.add(node)
            for cnode in adj_map[node]:
                if cnode != pnode and not dfs(cnode, node):
                    return False
            cycle.remove(node)
            adj_map[node] = []
            return True

        return False if not dfs(0,0) or self.visited != n else True