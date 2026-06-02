class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = defaultdict(list)

        for s, dst, wt in edges:
            adj[s].append((dst, wt))
        
        shortest = {}

        minheap = [(0, src)]

        while minheap:

            wt, src = heapq.heappop(minheap)

            if src in shortest:
                continue
            
            shortest[src] = wt
            
            for dst1, wt1 in adj[src]:
                if dst1 not in shortest:
                 heapq.heappush(minheap, (wt+wt1, dst1))

        # if nodes are not reachable 
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
                
        return shortest



