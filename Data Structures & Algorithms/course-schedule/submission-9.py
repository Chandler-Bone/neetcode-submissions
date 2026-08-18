class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preqMap[crs].append(preq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preqMap[crs] == []:
                return True

            visited.add(crs)
            for preq in preqMap[crs]:
                if not dfs(preq):
                    return False
                
            preqMap[crs] = []
            visited.remove(crs)

            return True    

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True