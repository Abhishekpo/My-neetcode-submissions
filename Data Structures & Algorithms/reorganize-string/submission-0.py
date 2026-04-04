class Solution:
    def reorganizeString(self, s: str) -> str:
        
        countdict={}
        for char in s:
            if char in countdict:
                countdict[char] +=1
            else:
                countdict[char] =1
        maxheap=[]
        for char, count in countdict.items():
            maxheap.append([-count, char])

        heapq.heapify(maxheap)
        ans =""
        prev=None

        while maxheap or prev:

            if prev and not maxheap:
                return ""

            count, char= heapq.heappop(maxheap)
            count +=1
            ans +=char

            if prev:
                heapq.heappush(maxheap, prev)
                prev=None
            if count <0:
                prev=[count, char]
        return ans

