class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        r=0
        curr_total=0
        maxval=nums[0]

        while r<len(nums):
            curr_total=max(curr_total, 0)
            curr_total=curr_total+nums[r]
            # if(curr_total <nums[r]):
            #     curr_total=nums[r]
            
            r+=1
            maxval=max(maxval, curr_total)
        return maxval
