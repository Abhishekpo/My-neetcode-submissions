class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mem={}
        def dfs(i):
            if i ==0:
                return nums[0]
            
            if i in mem:
                return mem[i]
            
            res=max(nums[i], nums[i]+dfs(i-1))

            mem[i]=res
            return res
        
        maxres=float('-inf')
        for i in range(len(nums)):
            maxres=max(maxres, dfs(i))

        return maxres

