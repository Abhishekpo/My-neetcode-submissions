class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l,r=0, 0
        total=0
        maxval=nums[0]

        while r<len(nums):
            total=total+nums[r]
            if(total <nums[r]):
                total=nums[r]
            
            r+=1
            maxval=max(maxval, total)
        return maxval
