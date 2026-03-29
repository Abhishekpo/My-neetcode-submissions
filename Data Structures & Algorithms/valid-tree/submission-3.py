class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        mymap={i:[] for i in range(n)}
        visit=set()

        for a, b in edges:
            mymap[a].append(b)
            mymap[b].append(a)

        def dfs(node, prev):

            if(node in visit):
                return False

            visit.add(node)

            for n in mymap[node]:

                if(n != prev):
                    if not dfs(n, node):
                        return False
                    visit.add(n)
            return True
        
        return dfs(0, -1) and  len(visit)==n
            