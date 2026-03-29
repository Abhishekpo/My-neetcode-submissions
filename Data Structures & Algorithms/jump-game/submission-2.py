class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(i):
            if(len(nums)-1==i):
                return True
            if(nums[i] ==0):
                return False
            for j in range(i+1, i+1+nums[i]):
                if(dfs(j)):
                    return True
            return False
        return dfs(0)
            
