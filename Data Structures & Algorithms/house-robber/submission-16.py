class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #first approach would be recursion
        #memoization 
        # this is tabulation
        # this is space optimization
        rob1=0
        rob2=0

        for i in range(0, len(nums)):
           temp=max(nums[i]+rob2, rob1)
           rob2=rob1
           rob1=temp
        return rob1

