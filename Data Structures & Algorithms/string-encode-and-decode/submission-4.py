class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=[]
        for st in strs:
            length=len(st)
            encode.append(f"{length}")
            encode.append("#")
            encode.append(st)
        return "".join(encode)
            



    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            count=""
            while s[i] !="#":
                count +=s[i]
                i +=1
            count=int(count)
            newstr=""
            for c in range(i+1, i+count+1):
                newstr +=s[c]
            result.append(newstr)
            i +=count+1
        return result



        
