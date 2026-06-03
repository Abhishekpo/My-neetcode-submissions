class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        row = len(heights)
        col = len(heights[0])
        directions = [[0,1],[1,0],[0, -1],[-1, 0]]

        visited = set()
        meanheap = [[0,0,0]]
       

        while meanheap:

            diff, r, c = heapq.heappop(meanheap)

            if (r, c) in visited:
                continue
            visited.add((r,c))

            if (r,c) == (row -1, col-1):
                return diff
            
            for dr, dc in directions:
                newdr , newdc = r + dr , dc + c
                if newdr < 0 or newdr == row or newdc == col or newdc < 0 or (newdr, newdc) in visited:
                    continue

                newcost = max(diff, abs(heights[r][c] - heights[newdr][newdc]))
                heapq.heappush(meanheap, [newcost, newdr, newdc])


            

            