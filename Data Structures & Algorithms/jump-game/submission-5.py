class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache=[False]*len(nums)
        cache[len(nums)-1]=True
        for i in range(len(nums)-2, -1,-1):
            for j in range(i, i+1+nums[i]):
                if(j<len(nums) and cache[j]):
                    cache[i]=True
        return cache[0]
                    
        