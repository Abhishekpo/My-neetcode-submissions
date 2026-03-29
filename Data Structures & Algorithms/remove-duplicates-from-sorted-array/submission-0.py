class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       myset=set()
       unique=[]
       for n in nums:
        if n not in myset:
            myset.add(n)
            unique.append(n)
       for i in range(len(unique)):
        nums[i]=unique[i]

       return len(unique)
