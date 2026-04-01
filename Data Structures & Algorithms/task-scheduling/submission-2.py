class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       
       count=Counter(tasks) # buil-in counter 
       maxheap=[-n for n in count.values()] # making values -negative from the dict

       heapq.heapify(maxheap)

       q=deque() # this queue act as a process stack in js async cycle
       cycle=0
       while maxheap or q:
        cycle +=1

        #if not maxheap: # just to make the process fast and empty the q fast not important
            #cycle =q[0][1]
        if maxheap:
            cnt=1 + heapq.heappop(maxheap)
            if cnt:
                next_process_time=cycle+n
                q.append([cnt, next_process_time])

        if q and q[0][1]==cycle:
            heapq.heappush(maxheap, q.popleft()[0])

       return cycle
             

