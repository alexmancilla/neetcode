class Node:
    def __init__(self, value, next_node = 0):
        self.value = value
        self.next = next_node

class LinkedList:
    # Dummy node
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.value
            i += 1
            current = current.next
        return -1


    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next 
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node 

        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head

        while i < index and current:
            i += 1
            current = current.next

        if current and current.next:
            # checking if its tail
            if current.next == self.tail:
                self.tail = current
            # assinging the new value 
            current.next = current.next.next
            return True
        return False



        

    def getValues(self) -> List[int]:
        current = self.head.next 
        res = []
        while current:
            res.append(current.value)
            current = current.next
        return res
        
