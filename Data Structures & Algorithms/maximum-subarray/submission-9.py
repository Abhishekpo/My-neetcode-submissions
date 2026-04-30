class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentsum=0
        maxvalue=float("-inf")
        for i in range(len(nums)):
            currentsum=max(nums[i], currentsum+nums[i])
            maxvalue=max(maxvalue, currentsum)
            
        return maxvalue
