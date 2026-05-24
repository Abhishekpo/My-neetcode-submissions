class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mydict={i: [] for i in range(numCourses)}

        for sub, pre in prerequisites:
            mydict[sub].append(pre)

        visited = set()
        oldvisited = set()

        def dfs(node):

            if node in visited:
                return False

            if node in oldvisited:
                return True

            visited.add(node)
            oldvisited.add(node)
            
            for n in mydict[node]:
                if not dfs(n):
                    return False
                    
            visited.remove(node)
            return True

        for i in range(numCourses):
            if i not in oldvisited:
             if not dfs(i):
                 return False

        return True

        
                
