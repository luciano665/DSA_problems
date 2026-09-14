class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Simple binary search
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            # Check num at mid is target if so return num at mid

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1


            elif nums[mid] < target:
                l = mid + 1


        # Target not in list
        return -1