class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        my_dic=[[] for i in range(n)]

        for a, b in edges:
            my_dic[a].append(b)
            my_dic[b].append(a)
        
        visit=set()

        def dfs(c, prev):

            if c in visit:
                return False
            
            visit.add(c)

            for nei in my_dic[c]:
                if nei==prev:
                    continue
                if not dfs(nei,c):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n

            