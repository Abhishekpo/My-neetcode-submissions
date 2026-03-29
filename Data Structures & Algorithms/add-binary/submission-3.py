class Solution:
    def addBinary(self, a: str, b: str) -> str:
    
     res= []
     r1=len(a)-1
     r2=len(b)-1
     carry=0
     while r1>=0 or r2>=0 or carry>0:
        digitA= int(a[r1]) if r1>=0 else 0
        digitB=int(b[r2]) if r2>=0 else 0

        total=digitA+digitB+carry
        if total %2==0:
            res.append("0")
        else:
            res.append("1")
        carry= total//2
        r1 -=1
        r2 -=1

     res.reverse()
     return "".join(res)
        
        
            
        