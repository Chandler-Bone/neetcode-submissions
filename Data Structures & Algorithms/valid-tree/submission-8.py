class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjMap = { i:set() for i in range(n) }

        for node, cnode in edges:
            adjMap[node].add(cnode)
            adjMap[cnode].add(node)

        # print(adjMap)

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if len(adjMap[node]) == 0:
                visited.add(node)
                return True
            
            visited.add(node)
            for cnode in adjMap[node]:
                adjMap[cnode].remove(node)
                if not dfs(cnode):
                    return False
            
            return True

        if not dfs(0):
            return False

        if len(visited) != n:
            return False
        
        return True