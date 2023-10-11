class Node:
    def __init__(self, key, val=-1, nex=None, prev=None):
        self.key = key
        self.val = val
        self.next = nex
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {}
        
    def addFirst(self, node):
        front = self.head.next

        self.head.next = node
        node.next = front
        node.prev = self.head
        front.prev = node 
    
    def removeLast(self):
        last = self.tail.prev

        self.tail.prev = last.prev
        last.prev.next = self.tail

        del self.hashmap[last.key]
    def remove(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def __repr__(self):
        curr = self.head
        arr = []

        while curr.next:
            arr.append(f'{curr.key}({curr.val})')
            curr = curr.next
        
        return ' -> '.join(arr)

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = LinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if key in self.cache.hashmap:
            node = self.cache.hashmap[key]

            self.cache.remove(node)
            self.cache.addFirst(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
       
        if key in self.cache.hashmap:
            node = self.cache.hashmap[key]
            node.val = value
            self.cache.remove(node)
        else:
            node = Node(key, value)
            self.cache.hashmap[key] = node
            
        self.cache.addFirst(node)
        if len(self.cache.hashmap) > self.capacity:
            self.cache.removeLast()
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)