class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        L = 0
        R = 0

        currentSum =0
        count =0
        prefixzero =0
        while R <len(nums):
            currentSum +=nums[R]

            while L < R and (nums[L] == 0 or currentSum > goal):

                if nums[L] == 0:
                    prefixzero +=1
                else:
                    prefixzero = 0

                currentSum -=nums[L]
                L+=1

            if currentSum == goal:
                count += 1 + prefixzero

            R +=1
           
           
        return count