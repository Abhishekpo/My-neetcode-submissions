class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        previous=0
        maxvalue=float('-inf')
        for i in range(len(nums)):
            previous=max(nums[i], nums[i]+previous)
            maxvalue=max(maxvalue, previous)
        return maxvalue



