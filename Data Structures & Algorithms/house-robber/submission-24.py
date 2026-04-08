class Solution:
    def rob(self, nums: List[int]) -> int:
     rob1=0
     rob2=0
     for num in nums:
        if rob2+num >rob1:
            temp=rob1
            rob1=rob2+num
            rob2=temp
        else:
            rob2=rob1

     return rob1
            
