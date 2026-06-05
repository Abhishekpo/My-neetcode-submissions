class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        adj = defaultdict(list)

        for st, dst1, cost in flights:
            adj[st].append((dst1, cost))

        minheap = [[0, src ,0]]
       
        while minheap:

            wt, s, flight_used = heapq.heappop(minheap)
            
            if s == dst:
                return wt

            if flight_used > k:
                continue
            
            for dst1, cost in adj[s]:
                 heapq.heappush(minheap, [cost+wt, dst1, 1+flight_used])

        return -1
                    




            
