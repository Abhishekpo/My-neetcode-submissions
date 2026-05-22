class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1

        queue = deque()
        queue.append("0000")
        visited = set(deadends)
        visited.add("0000")

        def produce_childof(currentseq):
            res=[]
            for i in range(len(currentseq)):
                newstrf = str((int(currentseq[i])+1)%10)
                newstrf = currentseq[:i] + newstrf + currentseq[i+1:]
                res.append(newstrf)

                newstrb = str((int(currentseq[i]) - 1 + 10) % 10)
                newstrb = currentseq[:i] + newstrb + currentseq[i+1:]
                res.append(newstrb)

            return res

        ans = 0
        while queue:

            for i in range(len(queue)):

                popq = queue.popleft()

                if popq == target:
                    return ans
                
                results = produce_childof(popq)

                for result in results:
                    if result not in visited:
                        visited.add(result)
                        queue.append(result)
            
            ans += 1

        return -1

                    
