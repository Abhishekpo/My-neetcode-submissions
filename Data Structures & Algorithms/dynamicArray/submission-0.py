class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr=[]
        self.capacity = capacity


    def get(self, i: int) -> int:
        for j in range(len(self.arr)):
            if j == i:
                return self.arr[i]

    def set(self, i: int, n: int) -> None:
        for j in range(len(self.arr)):
            if i == j:
                self.arr[i] = n


    def pushback(self, n: int) -> None:
        if len(self.arr) < self.capacity:
            self.arr.append(n)
        else:
            self.resize()
            self.arr.append(n)

    def popback(self) -> int:
        return self.arr.pop()
 
    def resize(self) -> None:
        self.capacity = 2 * self.capacity


    def getSize(self) -> int:
        return len(self.arr)
        
    def getCapacity(self) -> int:
        return self.capacity
