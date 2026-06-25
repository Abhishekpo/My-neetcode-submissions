class Solution:
    def rob(self, nums: List[int]) -> int:
        mem=[-1] * len(nums)
        def dfs(i):

         if i >= len(nums):
            return 0
         if mem[i] != -1:
            return mem[i]
         
         mem[i]= max(dfs(i+2)+nums[i], dfs(i+1))

         return mem[i]

        return dfs(0)