class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic={}
        
        for i in range(len(nums)):
            diff= target-nums[i]

            if diff not in mydic:
                mydic[nums[i]]=i
            else:
             return [mydic[diff],i]
        
