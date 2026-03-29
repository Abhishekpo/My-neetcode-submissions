class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic={}
        
        for i in range(len(nums)):
            diff= target-nums[i]

            if nums[i] not in mydic:
                mydic[diff]=i
            else:
             return [mydic[nums[i]],i]
        
