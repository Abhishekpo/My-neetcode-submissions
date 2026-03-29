class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj={i:[] for i in range(n)}
        

        for sc, dst, wt in edges:
            adj[sc].append((wt, dst))
        
        pq=[] # priority queue to store the shortes path node in mean+heap

        result={} # result dict to store the ans

        pq=[(0,src)]

        while pq:
            wt, node=heapq.heappop(pq)

            if(node in result):
                continue
            result[node]=wt

            for nei_wt, nei_node in adj[node]:
                if(nei_node not in result):
                    heapq.heappush(pq, (nei_wt+wt,nei_node))
            
        for i in range(n):
            if(i not in result):
                result[i]=-1

        return result
