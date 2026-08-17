class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not preMap[crs]:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            preMap[crs] = []

            return True

        for crs, prereq in prerequisites:
            if not dfs(crs):
                return False
        return True