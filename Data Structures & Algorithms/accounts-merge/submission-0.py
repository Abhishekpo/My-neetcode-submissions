class Disjoint:

        def __init__(self, n):
            self.parent = [i for i in range(n+1)]
            self.rank = [1] * (n+1)

        def find(self, node):
            p = node
            if self.parent[node] != node:
                p = self.find(self.parent[node])
            return p

        def union(self, first, second):

            first = self.find(first)
            second = self.find(second)

            if first == second:
                return False

            if self.rank[first] > self.rank[second]:
                self.parent[second] = first
                self.rank[first] += self.rank[second]
            else:
                self.parent[first] = second
                self.rank[second] += self.rank[first]

            return True

class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        obj = Disjoint(len(accounts))

        emailToAcc = {}

        for i, a in enumerate(accounts):

            for e in a[1:]:
                if e in emailToAcc:
                    obj.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list) # index of acc => list of emails

        for e, i in emailToAcc.items():
            leader = obj.find(i)
            emailGroup[leader].append(e)
        
        res = []

        for i, email in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res


        
    