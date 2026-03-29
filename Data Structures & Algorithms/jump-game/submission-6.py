class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache=[None]*len(nums)
        cache[len(nums)-1]=True
        def dfs(i):
            if(cache[i] is not None):
                return cache[i]
            if(nums[i] ==0):
                return False
            for j in range(i+1, i+1+nums[i]):
                cache[j]=dfs(j)
                if(cache[j]):
                    return cache[j]
            cache[i]=False
            return cache[i]
        return dfs(0)
            
