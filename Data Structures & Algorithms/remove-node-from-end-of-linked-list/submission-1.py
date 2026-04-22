# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 0

        while current:
            size += 1
            current = current.next
        
        # Paso 2: Caso especial - eliminar el primer nodo
        if size == n:
            return head.next  # Retorna el siguiente nodo como nueva cabeza

        new_n = size - n
        index = 0
        current = head

        while current and index < new_n - 1:
            current = current.next
            index += 1
        
        temp = current.next.next
        current.next = temp

        return head


        