# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # We will use a two pinter with a dummy node 
        # A left pointer starting at the dummy node
        # Right ptr at the head
        # We will move right until reach the nth node
        # We will move left until right is not null
        # Left ptr will end on the node before the nth node

        dummy = ListNode(0, head)
        left = dummy
        right = head

        
        while n > 0 and right:
            right = right.next
            n -= 1

        
        while right:
            left = left.next
            right = right.next

        # We are at the nth-1 node 

        #temp = left.next
        left.next = left.next.next
        #temp.next = None

        return dummy.next



        

        