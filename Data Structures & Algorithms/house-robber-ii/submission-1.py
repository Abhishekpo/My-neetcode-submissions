class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        rob1=0
        rob2=0


        for i in range(1, len(nums)):
            temp=rob2
            rob2=max(rob2, rob1+nums[i])
            rob1=temp
        rob3=0
        rob4=0
        for i in range(len(nums)-1):
            temp=rob4
            rob4=max(rob4, rob3+nums[i])
            rob3=temp
        return max(rob2, rob4)