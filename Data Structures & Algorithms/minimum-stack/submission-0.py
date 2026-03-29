class MinStack:

    def __init__(self):
        self.stack=[]
        self.minvalue=float("inf")
        

    def push(self, val: int) -> None:
        if self.stack:
            if val<self.minvalue:
                self.minvalue=val
            self.stack.append(val)
        else:
          self.stack.append(val)
          self.minvalue=val

        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

        
