class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap) >= 2:
            stone1 = abs(heapq.heappop(maxheap))
            stone2 = abs(heapq.heappop(maxheap))

            result = stone1 - stone2
            if result > 0:
                heapq.heappush(maxheap, -result)

        return abs(heapq.heappop(maxheap)) if len(maxheap) == 1 else 0 