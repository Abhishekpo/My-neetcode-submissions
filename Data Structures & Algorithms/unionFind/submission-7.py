class UnionFind:
    
    def __init__(self, n: int):
        self.parent=[i for i in range(n)]
        self.size =[0] * n
        self.count = n
        

    def find(self, x: int) -> int:
        p = self.parent[x]
        if p != x:
            self.parent[x]= self.find(self.parent[p])
            p = self.parent[x]

        return p
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        rootx= self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False

        self.count -= 1
        
        if self.size[rootx] < self.size[rooty]:
            self.parent[rootx] = rooty
            self.size[rooty] +=self.size[rootx]
            return True

        self.parent[rooty] = rootx
        self.size[rootx] += self.size[rooty]

        return True
        


    def getNumComponents(self) -> int:
        return self.count 


