class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # another way is to add all of the index and subtract the sum of nums to it
         # becaue the loop only goes upto len(nums)-1 index 
        #but we need to add uptolen(nums)
        res=len(nums)
        for i in range(len(nums)):
            res =res+i-nums[i]  # doing in one line what we are doing is [0,2,3] addig 0-3 index and addign that
        return res               # and adding 0+2+3 and subtracting 6-5=1

