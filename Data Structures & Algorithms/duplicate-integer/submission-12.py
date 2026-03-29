class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        myhash={}
        for n in nums:
            myhash[n] = 1 + myhash.get(n,0)
            if myhash[n]==2:
                return True
        return False