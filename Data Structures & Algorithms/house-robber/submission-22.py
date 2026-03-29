class Solution:
    def rob(self, nums: List[int]) -> int:
        # this is bottom-up


        res=[-1]*len(nums)
        
        def dfs(i):

         if(i<0):
             return 0

         if(res[i] != -1):
            return res[i]

         res[i]=max(dfs(i-1), dfs(i-2)+nums[i])
         return res[i]

        return dfs(len(nums)-1)
       


        