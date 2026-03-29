class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortedlist=sorted(nums)
        l=0
        r=1
        count=1
        maxcount=0
        while r<len(nums):
            if(sortedlist[l]+1==sortedlist[r]):
                count +=1
            else:
             if(sortedlist[l]!=sortedlist[r]):
                 maxcount=max(maxcount, count)
                 count=1
            l=r
            r=r+1
        maxcount=max(maxcount, count)
        return maxcount