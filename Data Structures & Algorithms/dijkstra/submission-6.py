class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = defaultdict(list)

        for s, dst, wt in edges:
            adj[s].append((dst, wt))

        shortest = {}
        for i in range(n):
            shortest[i] = float("inf")
            
        shortest[src] = 0
        minheap = [(0, src)]

        while minheap:

            wt, s = heapq.heappop(minheap)

            if wt > shortest[s]:
             continue
            
            for dst1, wt1 in adj[s]:
               if (wt1 + wt) < shortest[dst1]:
                 shortest[dst1] = wt1 +  wt
                 heapq.heappush(minheap, (wt1+wt, dst1))
                 
        # for unreachable nodes
        for i in range(n):
            if shortest[i] == float("inf"):
                shortest[i] =-1

        return shortest



