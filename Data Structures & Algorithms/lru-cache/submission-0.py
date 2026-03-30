class ListNode:
    def __init__(self, key, val):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} # hashmap

        self.left, self.right=ListNode(0,0) , ListNode(0,0) # value and used count
        self.left.next, self.right.prev =self.right, self.left

    def insert(self, node): # insert at the left
        right=self.left.next
        node.prev=self.left
        self.left.next=node
        node.next=right
        right.prev=node

    def remove(self, node):  # remove from the right
        leftnode=node.prev
        rightnode=node.next
        if leftnode: #we don't check this because self.right, self.left always exist 
         leftnode.next=rightnode
        if rightnode: #They are dummy nodes
         rightnode.prev=leftnode


    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            newnode=ListNode(key,value)
            self.cache[key]=newnode
            self.insert(newnode)

            if self.cap < len(self.cache):
                lru=self.right.prev
                self.remove(lru)
                del self.cache[lru.key]
             
        
        


        
