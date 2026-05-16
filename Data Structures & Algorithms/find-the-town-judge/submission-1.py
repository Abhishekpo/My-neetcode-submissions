class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing=defaultdict(int)
        incoming=defaultdict(int)
        for o, i in trust:
            outgoing[o] = 1 + outgoing.get(o, 0)
            incoming[i] = 1 + incoming.get(i, 0)
        
        for i in range(1, n+1):

            if  incoming[i] == n-1 and outgoing[i] == 0:
                return i
        return -1

