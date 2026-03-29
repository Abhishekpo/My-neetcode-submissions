class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        my_courses={i:[] for i in range(numCourses)}

        for src, dst in prerequisites:
            my_courses[src].append(dst)
        
        visit=set()
        
        def dfs(course):
            if course in visit:
                return False
            if(my_courses[course]==[]):
                return True
            
            visit.add(course)

            for nei in my_courses[course]:
                if not dfs(nei):
                    return False
            my_courses[course]=[]
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

