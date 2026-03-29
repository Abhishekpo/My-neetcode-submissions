class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum=-1e9
        for i in range(len(nums)):
            subarray_sum=0
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                maxsum=max(maxsum, subarray_sum)
        return maxsum