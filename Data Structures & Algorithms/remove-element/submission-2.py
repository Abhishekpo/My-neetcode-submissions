class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        L=0
        R=0

        for R in range(len(nums)):
            if(nums[R]!=val):
                temp=nums[R]
                nums[R]=nums[L]
                nums[L]=temp
                L+=1
        return L