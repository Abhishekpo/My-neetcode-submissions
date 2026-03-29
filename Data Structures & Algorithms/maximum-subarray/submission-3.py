class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum=-1e9
        currsum=-1e9
        for n in nums:
            if(currsum<=0):
                currsum=0
            currsum +=n
            maxSum=max(maxSum, currsum)
        return maxSum
