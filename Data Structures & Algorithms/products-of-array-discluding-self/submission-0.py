class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prefix =[0]*size
        postfix=[0]*size
        result=[0]*size
        
        prefix[0]=1
        for i in range(1, size):
            prefix[i]=prefix[i-1]*nums[i-1]
        postfix[size-1]=1
        for i in range(size-2, -1, -1):
            postfix[i]=postfix[i+1]*nums[i+1]
        for i in range(size):
            result[i]=postfix[i]*prefix[i]
        return result
            

            

            