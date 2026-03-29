class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr=""
        for s in strs:
            length=len(s)
            newstr += str(length)+ "#"+s
        return newstr 


    def decode(self, s: str) -> List[str]:
        i=0
        newlist=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j +=1
            length=int(s[i:j])
            newstr=s[j+1:j+1+length]
            newlist.append(newstr)
            i=j+1+length
        return newlist


