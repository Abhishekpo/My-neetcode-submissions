class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # The intution is that the all the duplicate elements would cancle eath other out
        # beacue of the xor ^ rule and only the distint element would be left
        res=0
        for n in nums:
            res= n ^ res
        return res