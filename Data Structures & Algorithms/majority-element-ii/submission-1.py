class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        mydict={}
        res=set()
        for num in nums:
            mydict[num]=1+mydict.get(num, 0)
            if mydict[num] >len(nums)//3:
                res.add(num)
        return list(res)
