class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
    
        curr_node =  self.get_node(index)
        
        if curr_node == -1:
            return -1
        
        return curr_node.value
    
    def get_node(self, index):
        i = 0
        curr_node = self.head
        if curr_node is None:
            return -1
        while i < index:
            curr_node = curr_node.next     
            i += 1
        
            if curr_node is None:
                return -1
        
        return curr_node
    
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        
        last_node = self.head
        
        if not last_node:
            self.head = new_node
            return 
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index-1)
            if prev_node != -1:
                new_node.next = prev_node.next
                prev_node.next = new_node
        
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index-1)
            if prev_node != -1:
                if prev_node.next:
                    prev_node.next = prev_node.next.next
                    
        
    def print_list(self):
        ls = []
        node = self.head
        while node:
            ls.append(str(node.value))
            node = node.next
            
        print("->".join(ls))
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)