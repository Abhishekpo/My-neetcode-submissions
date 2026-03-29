class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # this using two pointers 
        # so we are checking if l or right side is nearer which ever is farther we are skipping that
        # and moving ahead

        l, r= 0, len(arr)-1
        while r-l >= k: # same as doing (r-l)+1 !=k
            if abs(x-arr[l]) <=abs(x-arr[r]): # in terms of equal we are skipping right because 
                r -=1                         # in the sorted array right side will always be bigger.
            else:                             # if they are the same element it doesn't matter we can still remove the right
                l +=1

        return arr[l:r+1] # and here we do r+1 because in list r+1 noninclusive