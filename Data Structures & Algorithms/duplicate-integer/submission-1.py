class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         ansdic ={}
         for ele in nums:
            if ele in ansdic:
                return True
            else:
                ansdic[ele] =1
         return False