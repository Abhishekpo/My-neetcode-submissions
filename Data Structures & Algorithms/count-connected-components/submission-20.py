class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        my_dict={i:[] for i in range(n)}

        for src, dest in edges:
            my_dict[src].append(dest)
            my_dict[dest].append(src)
        visit=set()
        
        def dfs(node, parent):
            
            if node in visit:
                return False

            visit.add(node)
            for nei in my_dict[node]:
                if(nei==parent):
                    continue
                dfs(nei, node)
            return True
        total =0
        for i in range(n):
            if(dfs(i, -1)):
                total +=1
                
        return total



