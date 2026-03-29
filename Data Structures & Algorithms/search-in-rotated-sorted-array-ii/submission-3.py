class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        L=0
        R=len(nums)-1

        while L<=R:

            mid=(L+R)//2
            
            if nums[mid]==target:
                return True
            else:
                if nums[mid]>nums[L]: # mid is in left sorted portion
                    if target > nums[mid] or target < nums[L]:
                        L= mid+1
                    else:
                        R= mid-1
                
                elif(nums[mid]<nums[L]): # mid is in right sorted portion
                    if target < nums[mid] or target > nums[R]:
                        R= mid-1
                    else:
                        L= mid+1
                else:
                    L +=1


        return False

