class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window=set()
        L=0
        for R in range(len(nums)):
            if R-L >k: # we need to make the windo size intact so if it goes up we bring it down
                window.remove(nums[L])
                L +=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
            
