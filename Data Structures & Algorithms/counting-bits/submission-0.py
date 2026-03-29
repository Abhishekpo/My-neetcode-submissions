class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        def countbits(num):
            count =0
            while num:
                if num & 1:
                    count +=1
                num= num>>1

            ans.append(count)

        for i in range(0, n+1):
            countbits(i)

        return ans

