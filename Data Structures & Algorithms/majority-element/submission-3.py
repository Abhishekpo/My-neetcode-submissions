class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count=0
        res=0
        for n in nums:
            if(count==0):
                res=n
        
            if(res==n):
                count +=1
            else:
                count -=1
                
        return res # we dont have to do code below because there will always be 1 ans

        """
        count +=0
        for n in nums:
            if(n==res):
                count +=1
        if(count >len(nums)//2):
            return res
        return -1"""
