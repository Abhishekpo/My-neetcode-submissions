class UnionFind:
    
    def __init__(self, n: int):
        self.rank={}
        self.parents={}
        self.count=n

        for i in range(n+1):
            self.rank[i]=0
            self.parents[i]=i
        

    def find(self, x: int) -> int:
        p=self.parents[x]
        while p!=self.parents[p]:
            self.parents[p]=self.parents[self.parents[p]]
            p=self.parents[p]
        return p
        
    def isSameComponent(self, x: int, y: int) -> bool:
        x_parents=self.find(x)
        y_parents=self.find(y)
        return x_parents==y_parents

    def union(self, x: int, y: int) -> bool:
        x_parents=self.find(x)
        y_parents=self.find(y)

        if x_parents==y_parents:
            return False

        self.count -=1
        if self.rank[x_parents] < self.rank[y_parents]:
            self.parents[x_parents]=y_parents
        elif self.rank[y_parents] < self.rank[x_parents]:
            self.parents[y_parents]=x_parents
        else:
            self.parents[x_parents]=y_parents
            self.rank[y_parents] +=1

        return True
        

    def getNumComponents(self) -> int:
        return self.count


