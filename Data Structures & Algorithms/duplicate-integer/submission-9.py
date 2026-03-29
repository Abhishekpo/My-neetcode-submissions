class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #hashset
       '''mySet=set()
       
       for num in nums:
        if num in mySet:
            return True
        else:
            mySet.add(num)
       return False'''
       for i in range(len(nums)):
        for j in range(i+1,len(nums), 1):
            if(nums[i]==nums[j]):
             return True
       return False
