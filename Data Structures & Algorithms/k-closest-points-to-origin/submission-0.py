class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest=[]
        for x, y in points:
            dist=pow(x,2)+pow(y,2)
            closest.append([dist, x,y])
        heapq.heapify(closest)# this one compares using first value in the list
        res=[]
        while k:
            dist, x, y=heapq.heappop(closest) 
            res.append([x,y])
            k -=1
        return res

            

