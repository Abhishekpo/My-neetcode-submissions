class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans=0
        mem={}
        def dfs(rem): # number of possible combination of target

            if rem == 0:
                return 1

            if rem < 0:
                return 0

            if rem in mem:
                return mem[rem]

            ans=0

            for j in range(len(nums)):
                ans +=dfs(rem-nums[j])
                
            mem[rem]=ans
            return ans

        return dfs(target)
            


            