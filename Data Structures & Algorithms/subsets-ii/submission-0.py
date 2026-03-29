class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()
        def dfs(i, list1):

            if(i>=len(nums)):
                res.append(list1.copy())
                return
            list1.append(nums[i])

            dfs(i+1, list1)
            list1.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, list1)
            return
        dfs(0,[])
        return res