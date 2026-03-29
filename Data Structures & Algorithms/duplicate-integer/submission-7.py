class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #hashset
       ''' myset=set()
       for n in nums:
        if n in myset:
            return True
        else:
            myset.add(n)
       return False '''
       # Hash_map
       myhash={}
       for n in nums:
        if n in myhash:
            return True
        else:
            myhash[n] = 1
       return False
