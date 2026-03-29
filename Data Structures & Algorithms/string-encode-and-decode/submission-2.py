class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
         size=len(st)
         s += str(size)+"#"+st
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        c=0
        while c < len(s):
            num=""
            while s[c] !='#':
                num += s[c]
                c +=1
            num2 =int(num)
            st=""
            for i in range(c+1,c+1+num2):
                st +=s[i]
            res.append(st)
            c += num2+1

        return res

                


