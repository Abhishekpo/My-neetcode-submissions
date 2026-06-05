class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for i in range(len(points)):
         x1, y1 = points[i]
         for j in range(i+1, len(points)):
            x2, y2 = points[j]
            distance = abs(y2-y1) + abs(x2-x1)
            adj[i].append((distance, j))
            adj[j].append((distance, i)) 


        
        minheap=[(0, 0)]

        visited = set()
        total = 0
        while len(visited) < len(points):
            
            distance, src = heapq.heappop(minheap)

            if src in visited:
             continue

            visited.add(src)
            
            total += distance
            
            for distance, dst1 in adj[src]:
                if dst1 not in visited:
                 heapq.heappush(minheap, (distance, dst1))

        return total





        

