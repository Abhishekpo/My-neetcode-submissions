
class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
       self.stack.append(price)
       count =0
       if price <self.stack[-1]:
        return count
       else:
        newstack=[]
        for i in range(len(self.stack)):
            newstack.append(self.stack[i])
        while newstack and newstack[-1]<=price:
            newstack.pop()
            count +=1
       return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)