class UnionFind:
    # this one using size
    def __init__(self, n: int):
        self.size=[1]*n
        self.parents=[i for i in range(n)]
        self.count=n

        
    def find(self, x: int) -> int:
        if(x !=self.parents[x]):
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
        
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
        if self.size[x_parents] < self.size[y_parents]:
            self.parents[x_parents]=y_parents
            self.size[y_parents] +=self.size[x_parents]

        else:
            self.parents[y_parents]=x_parents
            self.size[x_parents] +=self.size[y_parents]

        return True
        

    def getNumComponents(self) -> int:
        return self.count


