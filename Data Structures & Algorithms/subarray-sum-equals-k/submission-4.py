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
       # so to reach the currentotal we must have subtracted the prefix amount
       # already in the back so we need to know how many times we have encounterd the 
       # currentprefix. we do that by curretprefix=K-currtotal
       # and check if it has been encoundered already and if yes get its count
       # that is our result so far. and keep adding to it going forward.
        mydict={0:1}
        currtotal=0
        res=0
        for n in nums:
         currtotal +=n 
         diff=currtotal-k # wahat we are doing here is we a
         res += mydict.get(diff, 0)

         mydict[currtotal]=1+mydict.get(currtotal, 0)

        return res
        
        