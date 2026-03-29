class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        
        indx=0
        for i in range(1, n):
            if abs(x-arr[indx]) > abs(x-arr[i]): # this finds you the narest element to the x
                indx=i

        ans=[arr[indx]] # which you put in a list and check outwars for other nearest elements
        L=indx-1 # this move outwards
        R=indx+1 # this also
        while len(ans)<k: # this checks if we have k number of elements already
            if L>=0 and R<n: # this checks if we have elements left in the right and left
                if abs(arr[L]-x) <= abs(arr[R]-x):
                    ans.append(arr[L])
                    L -=1
                else:
                    ans.append(arr[R])
                    R +=1
            elif L>=0: # if we have element in the left side add it until we get beyond k
                ans.append(arr[L])
                L-=1
            elif R<len(arr): # same thing if we dont have element in the left but we have in the right
                ans.append(arr[R])
                R+=1

        return sorted(ans) # sort the answer because we are puting elements in the list 
                            # randomly 

            