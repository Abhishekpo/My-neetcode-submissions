class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
    
        monoIncrease=True
        monoDecrease=True
        for i  in range(1, len(nums)):
           if nums[i-1] < nums[i]:
            monoDecrease=False
           if nums[i-1]>nums[i]:
            monoIncrease=False
        return monoIncrease or monoDecrease
                
       
            



            
