# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # We will need to add each number at the nodes starting from the edn (list-reversed)
        # We will need to keep track of a caryy if the sum is two-digits
        # Store each sum as a node

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            # Get vals if not set to 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Perform sum and update carry
            value = val1 + val2 + carry
            carry = value // 10
            # Need only single digit (no-carry)
            value = value % 10
            curr.next = ListNode(value)

            # Update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # Point to recent value added
            curr = curr.next

        # return the new list from head
        return dummy.next