class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force approch using two pointer:time complexity 
        for left in range(len(nums)):
         for right in range(left+1, len(nums), 1):
            if nums[left]+nums[right] == target:
                return [left,right]
        