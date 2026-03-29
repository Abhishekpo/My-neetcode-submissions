class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        size=len(nums)
        mydict={}
        res=set()
        for n in nums:
            mydict[n]=1+mydict.get(n, 0)
            if(mydict[n]>size//3):
                res.add(n)

        return list(res)