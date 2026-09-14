class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Will use slow and fast algo
        # We will detect a cycle if two vals in nums map to the same index
        # At index 0 never is linked to it
        # First pass need to find the intersection of the slow and fast
        # Second pass take another slow ptr and move by one until
            # The two slow ptrs intersect again 
        # Then we will have the value that is duplicate

        slow = 0
        fast = 0

        # First pass to find intersection of ptrs 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        # Second pass we have slow at intersection with fast ptr
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow2 == slow:
                # Find duplicate (cycle beginning)
                return slow2

        # Nothing duplicate in nums 
        return -1
