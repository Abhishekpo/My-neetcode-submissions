class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum=-1e9
        currsum=-1e9
        for n in nums:
            currsum=max(currsum, 0)
            currsum +=n
            maxSum=max(maxSum, currsum)
        return maxSum
