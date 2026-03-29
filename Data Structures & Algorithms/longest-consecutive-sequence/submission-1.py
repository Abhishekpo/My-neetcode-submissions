class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        myset=set(nums)
        res=0
        maxnum=max(nums)
        print(maxnum)
        minnum=min(nums)
        print(minnum)
        count=0
        for i in range(minnum, maxnum+1):
            if i in myset:
                count +=1
            else:
                count =0
            res=max(res, count)

        return res

