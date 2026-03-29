class ListNode:
 def __init__(self, val=-1, next=None):
    self.val=val
    self.next=next

class MyCircularQueue:
   
    def __init__(self, k: int):
        self.k=k
        self.front=ListNode()
        self.last=self.front
        self.count=0

    def enQueue(self, value: int) -> bool:
        if self.count <self.k:
         newnode=ListNode(value)
         self.last.next=newnode
         self.last=newnode
         self.count +=1
         return True

        return False


    def deQueue(self) -> bool:
        if self.front.next:
         self.front.next=self.front.next.next
         self.count -=1
         
         if self.count==0:
            self.last=self.front

         return True
        
        return False
        
    def Front(self) -> int:
        if self.front.next:
            return self.front.next.val
        return -1

        

    def Rear(self) -> int:
        if self.count>0:
            return self.last.val
        return -1
        

    def isEmpty(self) -> bool:
        if self.count ==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count>=self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()