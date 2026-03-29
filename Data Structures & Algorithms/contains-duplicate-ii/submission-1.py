class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mydict={}
        for i in range(len(nums)):
            if nums[i] in mydict and i-mydict[nums[i]] <= k:
                return True
            else:
                mydict[nums[i]] =i

        return False