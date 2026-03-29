class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        size=len(nums)
        mydict={}
        for n in nums:
            if n in mydict:
                mydict[n] +=1
            else:
                mydict[n]=1
            if(mydict[n]>size//2):
                return n
        
