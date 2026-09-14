# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Will solve this by div the list into 2 half
        # We find the half using a slow and fast pointer
            # Fast ptr will be pointing to the last node or null (if even or odd) 
            # Slow ptr will be the mid pointing at last val of first half
        # We must reverse the links on second half 
        # Each time we update pointers 

        slow = head
        fast = head.next

        # Find 2 half of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Beg of second half
        second = slow.next
        # Split of list
        slow.next = None 
        prev = None

        # Reverse of second portion
        while second:
            temp = second.next
            second.next = prev
            prev = second
            # End up pointing to null
            second = temp

        # Merge two halves
        second = prev
        first = head

        # We now the second half may be shorter so until second not null
        while second:
            # temp ptrs for saving current iter on 2 halfs
            temp1 = first.next
            temp2 = second.next

            # Merge operation
            first.next = second
            second.next = temp1

            # Update ptrs for next merge
            first = temp1
            second = temp2



