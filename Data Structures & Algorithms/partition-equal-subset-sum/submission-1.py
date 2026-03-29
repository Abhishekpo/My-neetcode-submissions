class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for i in range(len(nums)):
            total += nums[i]
        halftotal=total//2

        if total %2 !=0:
            return False
        
        

        def dfs(i, currtotal):
            
            if(currtotal ==halftotal):
                return True
            if(i>=len(nums) or currtotal> halftotal):
                return False
            
            return dfs(i+1, currtotal+nums[i]) or dfs(i+1, currtotal)
        return dfs(0, 0)

        