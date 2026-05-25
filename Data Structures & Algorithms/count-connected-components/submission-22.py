class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        visited = set()

        mygraph = {i:[] for i in range(n)}

        for start, end in edges:
            mygraph[start].append(end)
            mygraph[end].append(start)
        
        def dfs(node):
            
            if node in visited:
                return 

            visited.add(node)

            for nei in mygraph[node]:
                dfs(nei)
            
            return 

        count = 0
        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i)

        return count
        

            
            