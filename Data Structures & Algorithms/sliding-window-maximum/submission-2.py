class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """
        Brute force:
        In that window limit we we need to find max all the time and return it in a list
        using for loop.
        pseudo code for that would be:
        
        leftp=0
        Loop through the list with right pointer:

            if k == rightp-leftp +1
                maxvalue= max(nums[l:r+1])
                l +=1
                append maxvalue to the result
        return result

        This is O(n*k)

        Now Can we do better what is our bottel neck ?
        we had to calculate max of subarray all the time.
        what can we do to reduce the time complexity of that?

        I can think of the mootonic stack to find the max at each position

        
        """
        l=0
        ans=[]
        maxvalue= float("-inf")
        for r in range(len(nums)):
            

            if r-l+1 >= k:
                maxvalue = max(nums[l:r+1])
                l +=1
                ans.append(maxvalue)

        return ans


