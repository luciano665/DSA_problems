class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        # One L starting at 0 and one R at last element on list
        # Take sum of but and compare with target
        # Since is sorted from small to large
        # If sum > target decrement R and if sum < target increment L

        # Have an empty array to store result

        l = 0 
        r = len(numbers) - 1

        while l < r:

            # Must compute sum
            sumT = numbers[l] + numbers[r]

            # Check conditions
            if sumT < target:
                l += 1
            elif sumT > target:
                r -= 1

            else:
                return [l+1, r+1]