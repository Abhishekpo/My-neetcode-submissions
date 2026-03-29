class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        
        for i in range(len(nums)):
            if(nums[i]!=val):
                continue
            L=i
            R=i
            while R<len(nums):
                if(nums[R]!=val):
                    temp=nums[R]
                    nums[R]=nums[L]
                    nums[L]=temp
                    L=R
                R +=1
        k=0
        for num in nums:
            if num !=val:
                k+=1
        return k