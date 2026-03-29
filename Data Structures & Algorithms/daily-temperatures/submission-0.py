class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        mystack=[]
        ans=[0]*len(temperatures)
        for indx, temp in enumerate(temperatures):

            while mystack and mystack[-1][0] < temp:
                temp1, index1 =mystack.pop()
                ans[index1]=indx-index1
            
            mystack.append((temp, indx))
        return ans
