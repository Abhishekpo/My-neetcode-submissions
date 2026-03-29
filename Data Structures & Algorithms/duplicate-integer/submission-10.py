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
       """for i in range(len(nums)):
        for j in range(i+1,len(nums), 1):
            if(nums[i]==nums[j]):
             return True
       return False"""
       """newSet=set()
       for num in nums:
        if num in newSet:
         return True
        else:
         newSet.add(num)
       return False"""
       newhash={}
       for num in nums:
        if num in newhash:
            return True
        else:
            newhash[num] =1+newhash.get(num, 0)
       return False 

