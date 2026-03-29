class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greefy aproach

        size=len(nums)-1
        jump=size

        for i in range(size-1, -1,-1):
            if nums[i]+i >= jump:
                jump =i
        return jump==0