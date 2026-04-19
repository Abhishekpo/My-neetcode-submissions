class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total %2==0:
            target=total//2
        else:
            return False

        mem={}

        def dfs(sub, i):
            
            if sub == target:
                return True

            if i>=len(nums):
                return False


            if (sub, i) in mem:
                return mem[(sub,i)]

            
            skip= dfs(sub, i+1)
            if skip:
                mem[(sub, i)]=True
                return True

            take= dfs(sub+nums[i], i+1)
            if take:
                mem[(sub, i)]=True
                return True

            mem[(sub, i)]=False
            return False

        return dfs(0, 0)