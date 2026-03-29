class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        my_dic={i:[] for i in range(n)}
        res=0

        for a, b in edges:
            my_dic[a].append(b)
            my_dic[b].append(a)
        
        visit=set()
        
        def dfs(c):
            if c in visit:
                return
            if my_dic[c]==[]:
                return
            visit.add(c)

            for nei in my_dic[c]:
                dfs(nei)
            return

        for c in range(n):
            if c in visit:
                continue
            res +=1
            dfs(c)
        return res
            
            
            