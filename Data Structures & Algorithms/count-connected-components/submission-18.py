class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        mymap={i:[] for i in range(n)}
        visit=set()

        for s, d in edges:
            mymap[s].append(d)
            mymap[d].append(s)
            
        
        def dfs(node):
            if(node in visit):
                return 
            visit.add(node)
            for n in mymap[node]:
                dfs(n)
            return
        count =0
        for node in range(n):
            if node not in visit:
                 dfs(node)
                 count +=1
        return count

                
            