# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # We will use slow and fast pointer for cycle dectetion
        # If there is a cycle, both pointer will meet eventually
        # If no cycle fast pointer will point to null
        

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Detect if cycle
            if slow == fast:
                return True

        # return false if cyle was not detected
        return False
        