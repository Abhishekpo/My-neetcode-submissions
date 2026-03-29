class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        # this is true condition
        1->[3,2]
        2->[3]
        3->[]
        # this is false condition:cycle detected
        1->[3,2]
        2->[]
        3->[1]
        # This is disconnected : this is the reason we have to loop and dfs through
        each node and also delete the node after they return true from the set
        and empty the map[node]. because two subjects can have one prerequisits
        4->[5]
        3->[6]
        7->[5]
        6->[]
        """

        mymap={i:[] for i in range(numCourses)}
        visit=set()

        for cr, pre in prerequisites:
            mymap[cr].append(pre)
        
        def dfs(cr):
            if cr in visit:
                return False
            if mymap[cr]== []:
                return True
            visit.add(cr)

            for n in mymap[cr]: # this loops continues if return true and terminates if false
                                # it returns false back to prev call and that return false again
                                # to its previous call and the whole code returns false
                                # and terminates 
                if not dfs(n):
                    return False

            visit.remove(cr)
            mymap[cr]=[]
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
