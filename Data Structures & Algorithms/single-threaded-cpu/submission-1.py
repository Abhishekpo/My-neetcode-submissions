class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for indx, item in enumerate(tasks):
            item.append(indx)

        tasks.sort()

        ans=[]
        minheap=[]
        
        time=tasks[0][0]
        i=0
        while minheap or i<len(tasks):

            while i<len(tasks) and time >=tasks[i][0]:
                heapq.heappush(minheap, [tasks[i][1],tasks[i][2]])
                i+=1

            if not minheap:
                time =tasks[i][0]
            else:
                processtime, indx =heapq.heappop(minheap)
                time +=processtime
                ans.append(indx)

        return ans

            