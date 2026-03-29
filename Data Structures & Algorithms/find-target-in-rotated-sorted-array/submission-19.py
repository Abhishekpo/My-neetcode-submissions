class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L=0
        R=len(nums)-1

        while L<=R:

            mid=(L+R)//2
            
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]>=nums[L]: # mid is in left sorted portion
                    if target > nums[mid] or target < nums[L]: # this doesn't work for sorted array
                        L= mid+1
                    else:
                        R= mid-1
                
                else: # mid is in right sorted portion
                    if target < nums[mid] or target > nums[R]:
                        R= mid-1
                    else:
                        L= mid+1


        return -1

            