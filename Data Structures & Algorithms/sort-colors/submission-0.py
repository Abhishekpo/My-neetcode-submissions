class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partation(L, R):

            if(L>=R):
                return
            pivot=nums[R]
            left=L

            for i in range(L, R):
                if(nums[i]<pivot):
                    temp=nums[left]
                    nums[left]=nums[i]
                    nums[i]=temp
                    left +=1
            nums[R]=nums[left]
            nums[left]=pivot

            partation(L, left-1)
            partation(left+1, R)
        partation(0, len(nums)-1)
        return nums
        