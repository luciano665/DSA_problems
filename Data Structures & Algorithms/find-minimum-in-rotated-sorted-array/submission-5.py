class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Bin-Search for the nums arrays sorted but rotated after
        # There will be two part of the arrays where the min value may be
        # Both parts are sorted must find the correct part where min is
        # We will assume if sorted array after n rotation the first element will be the min
        # We took the mid the array if compare it to the left value
            # If the where to be >= mid -> we know that the mid val is part of the largest elements so we search on the left
            # Else we seach right -> since if mid is < R we know that the leeft part has the min val

        l = 0
        r = len(nums)-1
        res = nums[0]

        while l <= r:

            # Check if arr is sorted 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            # Compute the mid val
            m = (l+r) // 2
            res = min(res, nums[m])

            # Check if search left or right
            if nums[m] >= nums[l]:
                l = m + 1

            else:
                r = m - 1

            # recompute the min



        return res




       