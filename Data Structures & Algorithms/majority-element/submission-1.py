class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count=0
        res=0
        for n in nums:
            if(count==0):
                res=n
                count =1
            else:
                if(res==n):
                    count +=1
                else:
                    count -=1
        count +=0
        for n in nums:
            if(n==res):
                count +=1
        if(count >len(nums)//2):
            return res
        return -1
