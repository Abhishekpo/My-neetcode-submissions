class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing=True
        n=len(nums)
        for i in range(1, n): # checking increasing if nums[i-1]<=nums[i]

            if nums[i-1] >nums[i]: # if it fails dont continue terminate immediately 
                increasing=False
                break

        if increasing: # For loop runs completely and doesn't find False value
            return True

        decreasing=True
        for i in range(1, n): # checking decreasing if nums[i-1] >=nums[i]

            if nums[i-1] < nums[i]:  # this is increasing so terminate immediately
                decreasing= False
                break

        if decreasing:
            return True

        return False
                
       
            



            
