class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        ans=[]
        for ope in operations:
            if ope=="+":
                ans.append(int(ans[-1])+int(ans[-2]))
            elif ope=="C":
                ans.pop()
            elif ope=="D":
                ans.append(2*int(ans[-1]))
            else:
                ans.append(int(ope))
        return sum(ans)