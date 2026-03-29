class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      num1=set()
      for value in nums:
        if value in num1:
            return True
        else:
         num1.add(value)

      return False
      