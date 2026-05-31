class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # MAKE A TREE
        adj = defaultdict(list)
        for e1 , e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        def bfs(node):
            queue = deque()
            queue.append(node)

            visited = set()
            visited.add(node)
            height = 0

            while queue:

                for i in range(len(queue)):
                    popnode = queue.popleft()
                    for nei in adj[popnode]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
                height += 1
                

            return height

        
        minval = float("inf")
        myans = defaultdict(list)
        prev = float("inf")

        for i in range(n):
            res = bfs(i)
            if res <= prev:
                prev= res
            myans[res].append(i)

        return myans[prev]
    
        
        
            



        