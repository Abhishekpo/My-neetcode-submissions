class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum=nums[0]
        currsum=0
        for n in nums:
            currsum=max(currsum, 0)
            currsum +=n
            maxSum=max(maxSum, currsum)
        return maxSum
