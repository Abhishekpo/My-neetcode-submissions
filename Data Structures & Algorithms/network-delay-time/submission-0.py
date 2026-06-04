class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for s, d, w in times:
            adj[s].append((d, w))
        
        minheap = [[0, k]]

        visited=set()
        
        while minheap:

            wt, s = heapq.heappop(minheap)

            if s in visited:
                continue

            visited.add(s)

            if len(visited) == n:
                return wt

            for sn, wn in adj[s]:
                if sn not in visited:
                    heapq.heappush(minheap, [wn+wt, sn])

        return -1
            
