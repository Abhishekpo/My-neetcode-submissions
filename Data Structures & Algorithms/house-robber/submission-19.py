class Solution:
    def rob(self, nums: List[int]) -> int:
       
       if len(nums)<=2:
         return max(nums)
        
       rob1=0
       rob2=0
        
       for i in range(len(nums)):
            temp=rob2
            rob2=max(rob2, rob1+nums[i])
            rob1=temp
       return rob2


        