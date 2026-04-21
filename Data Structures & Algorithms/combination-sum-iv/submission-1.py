class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans=0
        mem={}
        def dfs(i, rem): # number of possible combination of target

            if rem == 0:
                return 1

            if rem < 0:
                return 0

            if i >= len(nums):
                return 0

            if (i, rem) in mem:
                return mem[(i, rem)]

            ans=0

            for j in range(len(nums)):
                ans +=dfs(j, rem-nums[j])
            mem[(i, rem)]=ans
            return ans

        return dfs(0, target)
            


            