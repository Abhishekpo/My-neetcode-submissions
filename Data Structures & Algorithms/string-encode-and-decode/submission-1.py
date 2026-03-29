class Solution:
    def encode(self, strs: List[str]) -> str:
        answer1=""
        for word in strs:
            answer1 += str(len(word)) +":"+ word

        return answer1
            

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decode=[]
        i=0
        while i< len(s):
            count=i
            while s[count] !=':':
                count +=1
                
            length1= int(s[i:count])
            i=count+1
            count=i+length1
            decode.append(s[i:count])
            i=count

            
        return decode