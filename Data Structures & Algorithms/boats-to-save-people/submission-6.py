class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # we can use counting sort sot sotr the array in O(N) make alfo O(n) insted of nlogn
        people.sort()
        res=0
        l=0
        r=len(people)-1

        while l<=r:
         remain=limit-people[r]
         r -=1
         res +=1
         if l<=r and remain >= people[l]:
             l +=1
        return res
