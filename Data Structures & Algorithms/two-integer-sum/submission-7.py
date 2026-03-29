class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force 
        myhash={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in myhash:
                return [myhash[diff], i]
            myhash[nums[i]]=i
    


            
        
        