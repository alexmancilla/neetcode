# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_pointer = dummy
        right_pointer = head

        for i in range(n):
            right_pointer = right_pointer.next

        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        
        left_pointer.next = left_pointer.next.next


        return dummy.next
        