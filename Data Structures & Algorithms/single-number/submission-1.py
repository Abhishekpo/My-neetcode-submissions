class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        mydict={}
        for n in nums:
            mydict[n]=1+mydict.get(n, 0)
        for key, value in mydict.items():
            if value==1:
                return key