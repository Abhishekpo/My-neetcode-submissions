class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we can do xor with every index and the element the element which is not will 
        # be left at the end
        xorr=len(nums)
        for i in range(len(nums)):
            xorr =xorr ^ i ^ nums[i]
        return xorr