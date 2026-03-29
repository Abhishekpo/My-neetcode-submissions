class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
       # we can do this problem optimally using prefix sum

        mydict={0:1}
        total=0
        res=0
        for n in nums:
         total +=n
         diff=total-k
         count= mydict.get(diff, 0)
         if count:
            res +=count

         mydict[total]=1+mydict.get(total, 0)

        return res
        
        