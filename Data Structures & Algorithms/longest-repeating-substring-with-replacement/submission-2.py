class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    #  result=0
    #  for i in range(len(s)):
    #     count, maxf= {}, 0
    #     for j in range(i, len(s)):
    #         count[s[j]]= 1 + count.get(s[j],0)
    #         maxf=max(count[s[j]], maxf)

    #         if (j-i+1)-maxf <=k:
    #             result=max(result, (j-i+1))
    #         else:
    #             break

    #  return result
     L=0
     result=0
     count, maxf= {},0
     for i in range(len(s)):
        count[s[i]]= 1+ count.get(s[i], 0)
        maxf= max(maxf, count[s[i]])

        # if (i-L+1)- maxf <=k: 
        #     result=max(result, (i-L+1))
        # else:
        #     count[s[L]] -=1
        #     L=L+1

        while (i-L+1)-maxf > k:
            count[s[L]] -=1
            L +=1
        result=max(result, (i-L+1))
     return result



