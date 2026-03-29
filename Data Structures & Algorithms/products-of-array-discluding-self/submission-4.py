class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prefix=[0]*size
        suffix=[0]*size
        for i in range(size):
            if i==0:
                prefix[i]=1
            else:
                prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(size-1,-1,-1):
            if i==size-1:
                suffix[i]=1
            else:
                suffix[i]=suffix[i+1]*nums[i+1]
        result=[]
        for i in range(size):
            result.append(prefix[i]*suffix[i])
        return result

    
        
        