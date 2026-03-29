class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #first approach would be recursion
        #memoization 
        # this is tabulation
        if(len(nums)==1):
            return nums[0]
        mem=[0 for i in range(len(nums)+1)]
        mem[0]=nums[0]
        mem[1]=max(nums[0], nums[1])

        for i in range(2, len(nums)):
            mem[i]=max(nums[i]+mem[i-2], mem[i-1])
        return mem[len(nums)-1]

