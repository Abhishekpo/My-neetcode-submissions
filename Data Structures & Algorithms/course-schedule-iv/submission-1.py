class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        mydict = {i :[] for i in range(numCourses)}

        for pre, cl in prerequisites:
            mydict[cl].append(pre)
        
        
        def dfs(node, pre, visited):

            if node == pre:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)
            
            for nei in mydict[node]:

                if dfs(nei, pre, visited):
                    return True


            return False

        ans = []
        for pre, cl in queries:
            ans.append(dfs(cl, pre, set()))

        return ans
            





            


            


