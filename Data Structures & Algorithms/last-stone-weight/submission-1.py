class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       maxHeap=[-s for s in stones]
       heapq.heapify(maxHeap)

       while len(maxHeap)>1:
            fstheaviest=heapq.heappop(maxHeap)
            sndheaviest=heapq.heappop(maxHeap)

            if fstheaviest < sndheaviest: # we check this because they might be equal
                heapq.heappush(maxHeap, fstheaviest-sndheaviest)

       return -maxHeap[0] if maxHeap else 0
