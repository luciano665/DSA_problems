class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) -1

        while l <= r:

            m = (l+r) // 2

            if nums[m] == target:
                return m

            
            # Left sorted portion 
            if nums[m] >= nums[l]:

                if target > nums[m] or target < nums[l]:
                    # Search right portion, target is not in left portion
                    l = m + 1
                else:
                    # Target was not on right portion
                    r = m - 1


            # Right sorted portion
            else:

                if target < nums[m] or target > nums[r]:
                    # Search left, target is not in right portion
                    r = m - 1
                else:
                    # Target was not on left portion
                    l = m + 1

                         
        return -1
