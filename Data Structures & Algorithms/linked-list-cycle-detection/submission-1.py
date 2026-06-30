# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        hare = head
        tortoise = head
        while hare.next and hare.next.next and tortoise.next:
            hare = hare.next
            hare = hare.next
            tortoise = tortoise.next
            if hare == tortoise: return True
        return False