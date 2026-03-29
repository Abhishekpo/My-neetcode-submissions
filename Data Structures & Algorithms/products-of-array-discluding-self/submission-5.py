class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        
        prefix=1
        postfix=1
        result=[1]*size
        for i in range(size):
            result[i]= prefix
            prefix *=nums[i]
        for i in range(size-1, -1,-1):
            result[i]=postfix*result[i]
            postfix *=nums[i]
        return result