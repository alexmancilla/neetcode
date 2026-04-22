# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hash_map = set()
        current = head

        while current:
            if current in hash_map:
                return True
            hash_map.add(current)
            current = current.next
        return False
        