class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L=0
        R=len(nums)-1

        while L<=R:
            mid=(L+R)//2
            if nums[mid]==target:
                return mid

            elif nums[mid] >= nums[L]: # we are in left portion
             if target > nums[mid] or target< nums[L]:
                L= mid+1
             else: # this is target < nums[mid] and target >nums[L]
                R =mid-1
                
            else: # we are in right portion
                if target < nums[mid] or target > nums[R]:
                    R =mid-1
                else: # target <nums[mid] and target<nums[L]
                    L=mid+1
        return -1

             
            
