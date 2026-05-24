class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mydict={i: [] for i in range(numCourses)}

        for sub, pre in prerequisites:
            mydict[sub].append(pre)

        

        def dfs(node, visited):

            if node in visited:
                return False

            visited.add(node)
            
            for n in mydict[node]:
                if not dfs(n, visited):
                    return False
            
            visited.remove(node)

            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True

        
                
