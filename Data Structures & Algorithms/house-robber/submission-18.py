class Solution:
    def rob(self, nums: List[int]) -> int:
       
       if len(nums)<=2:
         return max(nums)
        
       rob1=0
       rob2=0
        
       for i in range(len(nums)):
            if(rob1+nums[i]>rob2):
                temp=rob2
                rob2=rob1+nums[i]
                rob1=temp
            else:
                rob1=rob2
       return rob2


        