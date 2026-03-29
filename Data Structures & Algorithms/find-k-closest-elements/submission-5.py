class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        
        indx=0
        for i in range(1, n):
            if abs(x-arr[indx]) > abs(x-arr[i]):
                indx=i

        ans=[arr[indx]]
        L=indx-1
        R=indx+1
        while len(ans)<k:
            if L>=0 and R<n:
                if abs(arr[L]-x) <= abs(arr[R]-x):
                    ans.append(arr[L])
                    L -=1
                else:
                    ans.append(arr[R])
                    R +=1
            elif L>=0:
                ans.append(arr[L])
                L-=1
            elif R<len(arr):
                ans.append(arr[R])
                R+=1

        return sorted(ans)

            