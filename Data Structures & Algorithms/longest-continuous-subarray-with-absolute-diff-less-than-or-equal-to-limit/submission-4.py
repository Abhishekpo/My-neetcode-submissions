class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        for l in range(len(nums)):
            currmin = nums[l]
            currmax = nums[l]

            for r in range(l, len(nums)):
                currmin = min(currmin, nums[r])
                currmax = max(currmax, nums[r])

                if currmax - currmin <= limit:
                    res = max(res, r-l+1)

                else:
                    break

        return res
        