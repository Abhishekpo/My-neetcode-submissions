class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current=0
        maxvalue=float('-inf')
        for i in range(len(nums)):
            current=max(nums[i], nums[i]+current)
            maxvalue=max(maxvalue, current)
        return maxvalue



