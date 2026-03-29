class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1=0
        rob2=0
        count=0
        for i in range(len(nums)):
            
            if(nums[i]+rob2 > rob1):
                temp=rob1
                rob1=nums[i]+rob2
                rob2=temp
            else:
                rob2=rob1
                

        return rob1