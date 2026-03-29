class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        postfix=[0]*len(nums)
        res=[0]*len(nums)
        prefix[0]=1
        for i in range(1,len(nums),1):
            prefix[i] = prefix[i-1]*nums[i-1]
        postfix[len(nums)-1]=1
        for i in range(len(nums)-2, -1, -1):
            postfix[i]=postfix[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=prefix[i]*postfix[i]
        return res
        

