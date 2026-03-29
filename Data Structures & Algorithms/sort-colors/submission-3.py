class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        mydict=[0]*3
        for n in nums:
            mydict[n] +=1
       
        k=0
        for i in range(3):
           while mydict[i]:
            mydict[i] -=1
            nums[k] =i
            k+=1



        

