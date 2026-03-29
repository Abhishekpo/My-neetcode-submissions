class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        r1=len(a)-1
        r2=len(b)-1
        res=[]
        carry=False
        while r1>=0 and r2>=0:
            if a[r1]=="1" and b[r2]=="1":
                if carry:
                 res.append("1")
                 carry=True
                else:
                 res.append("0")
                 carry=True

            elif a[r1]=="1" or b[r2]=="1":
                if carry:
                 res.append("0")
                 carry=True
                else:
                    res.append("1")
            else:
                if carry:
                 res.append("1")
                 carry=False
                else:
                 res.append("0")

            r1 -=1
            r2 -=1

        while r1>=0:
                if a[r1]=="1":
                    if carry:
                     res.append("0")
                     carry=True
                    else:
                        res.append("1")
                else:
                    if carry:
                     res.append("1")
                     carry=False
                    else:
                     res.append("0")
                r1 -=1

        while r2>=0:
                if b[r2]=="1":
                    if carry:
                     res.append("0")
                     carry=True
                    else:
                        res.append("1")
                else:
                    if carry:
                     res.append("1")
                     carry=False
                    else:
                     res.append("0")
                r2 -=1

        if carry:
            res.append("1")

        res.reverse()
        return "".join(res)
        

