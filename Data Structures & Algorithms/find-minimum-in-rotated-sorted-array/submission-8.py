class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Invariant: one of [L..M] or [M..R] is sorted; the minimum lies in the unsorted half (unless nums[L] <= nums[R], then nums[L] is the min).
        # Decision rule: if nums[M] >= nums[L], left half is sorted → search right; else right half is sorted → search left.
        # Always track candidate answer: res = min(res, nums[M]); update pointers toward the unsorted half and recompute mid.

        # Pointers and assuming nums[0] is the min (array is sorted)
        l = 0
        r = len(nums) -1
        res = nums[0]

        while l<=r:

            # Check is array is already sorted after n rotation
            if nums[l] < nums[r]:
                res =  min(res, nums[l])
                break

            # Compute mid (array was not sorted)
            m = (l+r) // 2
            res = min(res, nums[m])

            # Find if min is on the left of right part
            if nums[m] >= nums[l]:
                # num at m is part of l -> search right
                l = m + 1
            else:
                # look left
                r = m -1

        return res