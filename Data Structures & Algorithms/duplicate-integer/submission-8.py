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
       # hashmap
       mymap={}
       for num in nums:
        mymap[num]= 1+ mymap.get(num,0)
       for num in nums:
        if mymap[num]>1:
            return True
       return False

