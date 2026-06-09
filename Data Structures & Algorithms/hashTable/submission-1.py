class Node:
    def __init__(self, key, value):
       self.value = value
       self.key = key
       self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.arr =[None] * capacity
        self.capacity = capacity
        self.size = 0
    
    def hashfunction(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        

        hashkey = self.hashfunction(key)

        if not self.arr[hashkey]:
            self.arr[hashkey] = Node(key, value)
            self.size +=1
        else:
            head = self.arr[hashkey]
            prev = None
            while head:
                if head.key == key:
                    head.value =value
                    return
                prev , head = head, head.next

            prev.next = Node(key, value)
            self.size +=1
        

        if self.size / self.capacity >= 0.5:
            self.resize()
            

    def get(self, key: int) -> int:
        hashkey = self.hashfunction(key)

        if self.arr[hashkey]:
            head = self.arr[hashkey]
            while head:
                if head.key == key:
                    return head.value
                head = head.next

        return -1


    def remove(self, key: int) -> bool:
        hashkey = self.hashfunction(key)
        head = self.arr[hashkey]
        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.arr[hashkey] = head.next
                self.size -=1
                return True

            prev , head = head, head.next

        return False
                
    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newcap = [None] * self.capacity

        for i in range(len(self.arr)):
            node = self.arr[i]
            while node:
               hashkey = self.hashfunction(node.key)
               if not newcap[hashkey]:
                 newcap[hashkey] = Node(node.key, node.value)
               else:
                 head = newcap[hashkey]
                 prev = None
                 while head:
                  prev , head = head, head.next

                 prev.next = Node(node.key, node.value)
               node = node.next

        self.arr = newcap
            
                
               
        

"""
 HashTable:
  I need a list to put keys addressess 
  To remove collision, I need a class/ node to store key value 
  

"""