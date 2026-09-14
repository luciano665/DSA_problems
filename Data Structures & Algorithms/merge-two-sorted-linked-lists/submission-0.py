# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Can use 2 pointer for traversing each list
        # Use a dummy node that will be the current head of combined sorted list
        # Compare each 2 pointers vals to be sorted
        # Move pointer on lists traversing if current node was added to new merged list
        # If one list is completed we just add the remaider of not complet list to new merged list

        # Base Case
        if not list1 and not list2:
            return None

        # Dummy and tail are init to val [0] as first node
        dummy = tail = ListNode()

        # While one of the lists is not empty
        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            # Tail must point do recent attached node
            tail = tail.next
        
        # Edge case add remaider of list
        tail.next = list1 or list2

        # Return merged list
        return dummy.next


        