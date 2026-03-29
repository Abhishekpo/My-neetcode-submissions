class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        nums=list(set(nums))
        nums.sort()
        count=1
        i=1
        maxcount=0
        if len(nums)==1:
            return 1
        while i<len(nums):
            if nums[i]==nums[i-1]+1:
                count +=1
            else:
                count =1
            maxcount=max(maxcount, count)
            i +=1
        return maxcount 
            
            

        