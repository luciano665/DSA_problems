# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Will use a two pointer approach
        # One prev and curr pointer
        # When curr pointer equals null, prev will be new head


        # Base case empty list
        if not head:
            return None


        curr = head
        prev = None

        # We loop until the end of the list
        while curr:
            # Temp var 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        # Return result new head is prev pointer
        return prev
