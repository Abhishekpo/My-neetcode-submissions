class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # we need to do xor a b this will give us value of addtion without
        # carry and to include the carry we do (a & b)<<1 and 
        # and check if we have carry if not return the xor result 
        # if yes do and with xor and carry to include carry and repeat
        mask=0xFFFFFFFF
        max_int = 0x7FFFFFFF

        carry=b
        while carry:
            xorresult= a^b
            carry= (a&b) <<1
            a=xorresult & mask
            b=carry & mask # to make them 32 bits because in python -ve value 
            # or bits are not 32 bits

        return a if a<=max_int else ~(a ^ mask)