class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float("-inf")
        currentmax = 1
        currentmin = 1
        for num in nums:
            tmp=currentmax
            currentmax = max(num, currentmax * num, currentmin * num)

            currentmin = min(num, tmp * num, currentmin * num)

            res= max(res, currentmax)

        return res
