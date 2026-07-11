class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """
        Brute force:
        In that window limit we we need to find max all the time and return it in a list
        using for loop.
        pseudo code for that would be:
        

        Loop through the list maintaining max value
            
            if k == r-l+1:
                maxvalue = max(nums[l:r+1])
                l +=1
            result.append(maxvalue)
        """
        result = []
        l = 0
        maxvalue =0
        for r in range(len(nums)):

            if k == r-l+1:
                maxvalue = max(nums[l:r+1])
                l +=1
                result.append(maxvalue)

        return result
