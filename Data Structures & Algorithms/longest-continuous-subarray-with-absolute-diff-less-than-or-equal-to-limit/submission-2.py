class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        '''
        so I have an array 
        i have to generate all the sumarray such that each element in the sub array is 
        less than or equal to the limit.


        '''

        def dfs(i, arr):

            if i >= len(nums):
                return len(arr) 
            
            for j in range(len(arr)):
                if abs(arr[j] - nums[i]) > limit:
                    return len(arr)

            arr.append(nums[i])
            return dfs(i+1, arr )

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i+1, [nums[i]]))

        return ans



                    