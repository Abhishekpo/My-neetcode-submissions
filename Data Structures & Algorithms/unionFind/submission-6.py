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
            self.parent[x] = rooty
            self.size[rooty] +=1
            return True

        self.parent[y] = rootx
        self.size[rootx] +=1

        return True
        


    def getNumComponents(self) -> int:
        return self.count 


