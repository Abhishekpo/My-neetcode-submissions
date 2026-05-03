class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left  = 0
        total = 0
        right = 0

        while right <len(nums)-1:
            jump=0 # to keep track of the local jump in the jump window range
            for j in range(left, right+1):
                jump=max(jump, right + nums[j])

            left=right+1
            right=jump
            total +=1

        return total
            


            
            