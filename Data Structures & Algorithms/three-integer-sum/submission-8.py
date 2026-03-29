class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        nums.sort()
        newset=set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
             for k in range(j+1, len(nums)):
                target=nums[i]+nums[j]+nums[k]

                if(target==0):
                    targetset=(nums[i], nums[j], nums[k])
                    newset.add(targetset)

        return [list(i) for i in newset]
        
