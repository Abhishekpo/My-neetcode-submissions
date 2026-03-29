class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mydict=defaultdict(int)
        for i in range(len(nums)):

            if mydict[nums[i]] and i-(mydict[nums[i]]-1) <= k:
                return True
            else:
                mydict[nums[i]] =i+1

        return False