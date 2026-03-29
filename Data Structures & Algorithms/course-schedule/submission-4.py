class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        my_dic= {i:[] for i in range(numCourses)}
        # first figure out how to reperesnt your graph 
        # and what are the base cases, like cycle detection, or 
        # component detetction and if one condition fails dont check further.

        for a,b in prerequisites:
            my_dic[a].append(b) # we are not doing my_dic[b].append(a)
            # because in this case that is a cycle b will come seperatly
            # example to take a we have to take b and similarly if b has
            # any prerequisites it will be given seperatly
        
        visit= set() # for cycle detection

        
        def dfs(c):
            if c in visit:
               return False
            if my_dic[c]==[]:
                return True

            visit.add(c)

            for nei in my_dic[c]:
                if not dfs(nei):
                 return False
            visit.remove(c)
            my_dic[c]=[]
            return True      
            

        for c in range(numCourses):
             if not dfs(c):
                return False
        return True




