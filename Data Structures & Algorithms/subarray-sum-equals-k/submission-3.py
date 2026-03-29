class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
       # we can do this problem optimally using prefix sum
       # the idea is as we go ahead we also save what prefix sums we 
       # encountered on the way and its count because if we know the prefix 
       #sums at each index before what we could do is. we will know the current total
       # if we find a currtotal that adds to the prefix gives us the value we looking
       # for than we can make that value k, the count times. adding that prefix to
       # our currenttotal
       # currtotal+ prefix=k
       # so, currtotal-k= -prefix
       # so to reach the currentotal we must have encounterd the prefix of
       # k-currenttoal 
        mydict={0:1}
        currtotal=0
        res=0
        for n in nums:
         currtotal +=n 
         diff=currtotal-k # wahat we are doing here is we a
         res += mydict.get(diff, 0)

         mydict[currtotal]=1+mydict.get(currtotal, 0)

        return res
        
        