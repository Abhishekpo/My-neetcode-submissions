class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        adj=defaultdict(list)
        for src, dst, wt in edges:
            adj[src].append((wt,dst))
            adj[dst].append((wt,src))
        
        pq=[]
        for wt, nei in adj[0]:
         heapq.heappush(pq,(wt, 0, nei))

        visited=set()
        visited.add(0)
        mst=[]
        total=0
        while pq and len(visited)<n:
            wt, src, dst =heapq.heappop(pq)
            if dst in visited:
                continue
            total +=wt
            visited.add(dst)
            mst.append((src, dst))
            for wt2, nei in adj[dst]:
                if(nei not in visited):
                    heapq.heappush(pq, (wt2, dst, nei))
        return total if len(visited)==n else -1

