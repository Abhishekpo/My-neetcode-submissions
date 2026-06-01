class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]

        adj = defaultdict(list)

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        leaves = deque()
        adj_count = {}

        for i in range(n):
            adj_count[i] = len(adj[i])
            if len(adj[i]) == 1:
                leaves.append(i)
        
        

        while leaves:

            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1

                for nei in adj[leaf]:
                    adj_count[nei] -= 1
                    if adj_count[nei] == 1:
                        leaves.append(nei)
            
        
                


            


            

        
        