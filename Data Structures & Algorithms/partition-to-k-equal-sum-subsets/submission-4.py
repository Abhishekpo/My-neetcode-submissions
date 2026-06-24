class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k

        visited = [False] * len(nums)

        def dfs(i, k, currsum):

            if k == 0:
                return True
            
            if currsum == target:
                if dfs(0, k-1, 0):
                    return True
            
            for j in range(i, len(nums)):

                if visited[j]:
                    continue 
                
                if nums[j] + currsum > target:
                    continue

                visited[j] = True
                if dfs(j+1, k, currsum + nums[j]):
                    return True

                visited[j] = False

            return False

        return dfs(0, k, 0)
    

                
                
