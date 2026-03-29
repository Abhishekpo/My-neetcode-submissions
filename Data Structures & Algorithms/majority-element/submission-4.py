class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # what we could do is: 
        L=0
        R=0
        count =0
        majority=0
        for R in range(len(nums)):
            if count ==0:
                majority=nums[R]
            if(majority==nums[R]):
                count +=1
            else:
                count -=1
        return majority