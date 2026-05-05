class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        total=0
        maxlen=1
        prev=""
        for i in range(1, len(arr)):
    
            if prev == ">":
                if arr[i]<arr[i-1]:
                    total +=1
                    prev="<"
                elif arr[i]>arr[i-1]:
                    prev =">"
                    total =2
                else:
                    prev="="
                    total =1
                    
                
            elif prev =="<":
                if arr[i] > arr[i-1]:
                    total +=1
                    prev=">"
                elif arr[i]<arr[i-1]:
                    prev ="<"
                    total =2
                else:
                    prev= "="
                    total =1
            else:
                if arr[i]<arr[i-1]:
                    prev = "<"
                elif arr[i]>arr[i-1]:
                    prev =">"
                
                if arr[i] !=arr[i-1]:
                 total=2
                else:
                 total=1

            maxlen=max(total, maxlen)
                    
        return maxlen
             


            
