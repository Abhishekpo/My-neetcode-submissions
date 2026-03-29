class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #first approach would be recursion
        #memoization 
        mem=[0 for i in range(len(nums)+1)]

        def dfs(i):

            if(i>=len(nums)):
                return 0
            if(mem[i]):
                return mem[i]
            
            left=nums[i] + dfs(i+2)
            right=dfs(i+1)
            mem[i]= max(left, right)
            return mem[i]

        return dfs(0)


