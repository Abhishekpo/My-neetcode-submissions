class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        mydict = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            mydict[course].append(pre)
        
        visited_inall = set()
        visited = set()
        ans = []

        def dfs(course):

            if course in visited:
                return False
            
            visited.add(course)
            
            
            

            for pre in mydict[course]:

                if not dfs(pre):
                    return False
                    
            if course not in visited_inall:
                ans.append(course)

            visited_inall.add(course)
            visited.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans
            

                

            
            
