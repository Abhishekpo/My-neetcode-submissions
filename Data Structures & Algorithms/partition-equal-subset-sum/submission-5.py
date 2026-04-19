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
            
            if sub >target: # to ecexute early
                return False

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
        #cleaner version if anyone brings true return true
        # mem[(sub, i)]=dfs(sub, i+1) or dfs(sub+nums[i], i+1) short circuit
        # return mem[(sub, i)]
        return dfs(0, 0)