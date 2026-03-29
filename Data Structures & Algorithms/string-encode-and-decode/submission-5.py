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
            count=i
            while s[count] !="#":
                count +=1
            length=int(s[i:count])
            i=count+1
            count=i+length
            result.append(s[i:count])
            i=count
        return result



        
