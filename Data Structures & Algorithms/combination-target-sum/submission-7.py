class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # so i produce all the combinations and gets there total and if the total
        # is == target i register that.
        res = []

        def dfs(total, i, arr):

            if total == target:
                res.append(arr.copy())
                return
                
            if total > target:
                return 
            
            for j in range(i, len(nums)):
                arr.append(nums[j])
                dfs(total + nums[j], j, arr)
                arr.pop()

        dfs(0, 0, [])
        return res
