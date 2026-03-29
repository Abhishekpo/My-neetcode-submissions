class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        first=nums[0]
        monoIncrease=True
        monoDecrease=True
        for i  in range(1, len(nums)):
            if first <= nums[i]:
                first=nums[i]
            else:
                monoDecrease=False

        first=nums[0]
        for i in range(1, len(nums)):
            if first >=nums[i]:
                first=nums[i]
            else:
                monoIncrease=False
        
        return monoIncrease or monoDecrease
                
       
            



            
